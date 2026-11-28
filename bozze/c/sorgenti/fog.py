import bpy,sys,numpy as np
S=int(sys.argv[1]) if len(sys.argv)>1 else 640
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.device='CPU';sc.cycles.samples=8;sc.cycles.use_denoising=False
sc.render.resolution_x=S;sc.render.resolution_y=S;sc.render.film_transparent=True
sc.view_settings.view_transform='Standard'
sc.cycles.volume_bounces=2
bpy.ops.mesh.primitive_plane_add(size=8,location=(0,0,0));pl=bpy.context.object
m=bpy.data.materials.new('f');m.use_nodes=True;nt=m.node_tree;nt.nodes.clear()
out=nt.nodes.new('ShaderNodeOutputMaterial');mixs=nt.nodes.new('ShaderNodeMixShader')
tr=nt.nodes.new('ShaderNodeBsdfTransparent');em=nt.nodes.new('ShaderNodeEmission');em.inputs[0].default_value=(.94,.97,1,1);em.inputs[1].default_value=1
tc=nt.nodes.new('ShaderNodeTexCoord')
def noise(sc,det,dist,rough,stretch=(1,1,1),off=(0,0,0)):
    mp=nt.nodes.new('ShaderNodeMapping');mp.inputs['Scale'].default_value=stretch;mp.inputs['Location'].default_value=off
    n=nt.nodes.new('ShaderNodeTexNoise');n.noise_dimensions='3D';n.inputs['Scale'].default_value=sc;n.inputs['Detail'].default_value=det;n.inputs['Distortion'].default_value=dist;n.inputs['Roughness'].default_value=rough
    nt.links.new(tc.outputs['Object'],mp.inputs['Vector']);nt.links.new(mp.outputs[0],n.inputs['Vector']);return n.outputs['Fac']
big=noise(.55,5,1.2,.55,(.8,1.5,1));fine=noise(1.6,6,.8,.6,(.7,1.4,1),(3,1,0))
def ramp(inp,a,b):
    r=nt.nodes.new('ShaderNodeValToRGB');r.color_ramp.elements[0].position=a;r.color_ramp.elements[1].position=b;nt.links.new(inp,r.inputs[0]);return r.outputs[0]
d1=ramp(big,.30,.68);d2=ramp(fine,.25,.80)
mA=nt.nodes.new('ShaderNodeMath');mA.operation='MULTIPLY_ADD';nt.links.new(d2,mA.inputs[0]);mA.inputs[1].default_value=.55;mA.inputs[2].default_value=.45
mB=nt.nodes.new('ShaderNodeMath');mB.operation='MULTIPLY';nt.links.new(d1,mB.inputs[0]);nt.links.new(mA.outputs[0],mB.inputs[1])
mC=nt.nodes.new('ShaderNodeMath');mC.operation='MULTIPLY';mC.inputs[1].default_value=.85;nt.links.new(mB.outputs[0],mC.inputs[0])
nt.links.new(mC.outputs[0],mixs.inputs[0]);nt.links.new(tr.outputs[0],mixs.inputs[1]);nt.links.new(em.outputs[0],mixs.inputs[2]);nt.links.new(mixs.outputs[0],out.inputs[0])
pl.data.materials.append(m)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam
cam.data.type='ORTHO';cam.data.ortho_scale=6;cam.location=(0,0,5)
sc.render.filepath='/tmp/fog_raw.png';bpy.ops.render.render(write_still=True)
a=np.array(bpy.data.images.load('/tmp/fog_raw.png').pixels[:]).reshape(S,S,4)
# rendi seamless in x e y
def seam(a):
    n=a.shape[1];x=np.linspace(0,1,n);wgt=np.sin(np.pi*x)**2
    return a*wgt[None,:,None]+np.roll(a,n//2,axis=1)*(1-wgt)[None,:,None]
a=seam(a);a=seam(a.transpose(1,0,2)).transpose(1,0,2)
al=a[...,3];print('alpha mean',al.mean(),al.max())
np.save('/tmp/fog.npy',a)
