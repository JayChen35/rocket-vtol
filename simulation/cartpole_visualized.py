#!/usr/bin/env python
"""Chain example using the visualizer.

This is the same example as provided in [1], but translated into Python and using the `raisimpy` library (which
is a wrapper around `raisimLib` [2] and `raisimOgre` [3]).

References:
    - [1] https://github.com/leggedrobotics/raisimOgre/blob/master/examples/src/robots/chain.cpp
    - [2] raisimLib: https://github.com/leggedrobotics/raisimLib
    - [3] raisimOgre: https://github.com/leggedrobotics/raisimOgre
"""

import os
import numpy as np
import raisimpy as raisim


def normalize(array):
    return np.asarray(array) / np.linalg.norm(array)


def setup_callback():
    vis = raisim.OgreVis.get()
    print("Recording saving to:", vis.get_resource_dir())

    # light
    light = vis.get_light()
    light.set_diffuse_color(1, 1, 1)
    light.set_cast_shadows(True)
    vis.get_light_node().set_direction(normalize([-3., -3., -0.5]))
    vis.set_camera_speed(300)

    # load textures
    vis.add_resource_directory(vis.get_resource_dir() + "/material/checkerboard")
    vis.load_material("checkerboard.material")

    # shadow setting
    manager = vis.get_scene_manager()
    manager.set_shadow_technique(raisim.ogre.ShadowTechnique.SHADOWTYPE_TEXTURE_ADDITIVE)
    manager.set_shadow_texture_settings(2048, 3)

    # scale related settings!! Please adapt it depending on your map size
    # beyond this distance, shadow disappears
    manager.set_shadow_far_distance(10)
    # size of contact points and contact forces
    vis.set_contact_visual_object_size(0.03, 0.2)
    # speed of camera motion in freelook mode
    vis.get_camera_man().set_top_speed(5)


def keymapping(event):
    global force
    RIGHT = 1073741903
    LEFT = 1073741904
    DOWN = 1073741905
    UP = 1073741906
    sym = event.keysym.sym
    print(sym)
    if sym == LEFT:
        force[0] = -100
    elif sym == RIGHT:
        force[0] = 100
    elif sym == UP:
        force[1] = 100
    elif sym == DOWN:
        force[1] = -100
    return

def controlmapping() -> None:
    global plate, force
    plate.set_external_force(1, np.array([force[0], force[1], 0]))


if __name__ == '__main__':
    # create raisim world
    time_step = 0.01
    world = raisim.World()
    world.set_time_step(time_step)
    world.set_erp(world.get_time_step() * 0.1, world.get_time_step() * 0.1)

    vis = raisim.OgreVis.get()

    # these methods must be called before initApp
    vis.set_world(world)
    vis.set_window_size(1800, 900)
    vis.set_default_callbacks()
    vis.set_setup_callback(setup_callback)
    vis.set_anti_aliasing(8)

    # init
    vis.init_app()

    offset = 0.5
    height = 7
    width = 6
    radius = 0.5

    # create raisim objects
    ground = world.add_ground()
    global plate, cylinder, force
    plate = world.add_box(x=width, y=width, z=offset, mass=5)
    cylinder = world.add_cylinder(radius=radius, height=height, mass=1)
    force = [0, 0]
    plate.set_position(0, 0, offset / 2)
    cylinder.set_position(0, 0, offset + height / 2)
    cylinder.set_orientation(1, 0, 0, 0)
#    cylinder.set_orientation(1, 0.5, 0, 0)
#    ball = world.add_sphere(radius=1, mass=2)

    # create visualizer objects
    vis.create_graphical_object(ground, dimension=50, name="floor", material="default")
    vis.set_keyboard_callback(keymapping)
    vis.set_control_callback(controlmapping)
#    ball_graphics = vis.create_graphical_object(ball, name="ball", material="default")
    plate_graphics = vis.create_graphical_object(plate, name="plate", material="blue")
    cylinder_graphics = vis.create_graphical_object(cylinder, name="cylinder", material="yellow")

    print(cylinder.get_position())

    vis.select(cylinder_graphics[0])
    vis.get_camera_man().set_yaw_pitch_dist(0., -np.pi / 4., 20)
    print(type(vis.get_camera_man()))


#    ball.set_position(0, 0, 200)

    # run the app
    vis.run()

    # terminate
    vis.close_app()
