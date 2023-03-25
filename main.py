import bpy
from random import randint

removeThese = bpy.context.copy()
removeThese['selected_objects'] = list(bpy.context.scene.objects)
bpy.ops.object.delete(removeThese)

fbx_path = '/Users/jessesnyder/code/3dmodeling/eyeball/16_eye.fbx'
bpy.ops.import_scene.fbx(filepath=fbx_path)

def duplicate(obj):
    obj_copy = obj.copy()
    obj_copy.data = obj_copy.data.copy()
    bpy.context.collection.objects.link(obj_copy)
    return obj_copy

x_location = 0
y_location = 0
z_location = 0
x_rotation = 0
y_rotation = 0
z_rotation = 0
x_scale = 100
y_scale = 100
z_scale = 100
imported_object = bpy.context.selected_objects[0]
imported_object.location = (x_location, y_location, z_location)
imported_object.rotation_euler = (x_rotation, y_rotation, z_rotation)
imported_object.scale = (x_scale, y_scale, z_scale)

def generate_eyes():
    print('wtf')
    for i in range(3):
        copy = duplicate(imported_object)
        copy.location = tuple([randint(-50, 50) for axis in 'xyz'])
    return 1

#def generate_cubes():
#    for i in range(3):
#        bpy.ops.mesh.primitive_cube_add(
#            location=[randint(-10, 10) for axis in 'xyz'])
#    return 1

bpy.app.timers.register(generate_eyes)
