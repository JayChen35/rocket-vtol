#!/usr/bin/env python
# UR RETARDED AND PROLLY GONNA FORGET THIS, BUT USE THE TERMINAL IN MOBA X TERM, NOT JUST THE X SERVER
"""Chain example using the visualizer.

This is the same example as provided in [1], but translated into Python and using the `raisimpy` library (which
is a wrapper around `raisimLib` [2] and `raisimOgre` [3]).

References:
    - [1] https://github.com/leggedrobotics/raisimOgre/blob/master/examples/src/robots/chain.cpp
    - [2] raisimLib: https://github.com/leggedrobotics/raisimLib
    - [3] raisimOgre: https://github.com/leggedrobotics/raisimOgre
"""

import os
import math
import numpy as np
import raisimpy as raisim
from helpers import setup_vis, quaternion_to_euler
from pidhandler import PDHandler

np.set_printoptions(precision=2)

RIGHT = 1073741903
LEFT = 1073741904
DOWN = 1073741905
UP = 1073741906

# Drone properties
height = 2
width = 7
mass = 0.5
mr = 2.5 # Motor radius
tilt = 45

time_step = 0.01

PDs = [PDHandler(1.8, .5, time_step), PDHandler(-1.8, -.5, time_step)]

global mode, drone
#mode = ord('w')
mode = -1

def keymapping(event):
    global mode
    sym = event.keysym.sym
    if sym in [ord('w'), ord('a'), ord('s'), ord('d'), UP, DOWN, ord(' ')]:
        mode = event.keysym.sym


def stabilize():
    vel = drone.get_world_linear_velocity(1)[2]
    if vel == 0:
        return np.zeros((4,3))
    elif vel > 0:
        return np.array([np.array([0, 0, -50])] * 4)
    else:
        return np.array([np.array([0, 0, 50])] * 4)

global MAXFORCE
MAXFORCE = 0
def alt_hold_force(angle):
#    angle = 2 * math.acos(quat[0])
#    orientation = quaternion_to_euler(*quat)
#    angle = -orientation[1]
    mg = mass * world.get_gravity()[2]
    Fy = -mg
    F = Fy / math.cos(angle * math.pi / 180)
    return F

def calc_stuff(orientation, target, idx):
    dist = target - orientation
    p, d, torque = PDs[idx].calculate(dist[2-idx])
    print("Torque:", torque)
    F = alt_hold_force(orientation[2-idx])
    dF = torque / (2 * mr)
    force_vec = np.array([0, 0, F + dF])
    less_vec = np.array([0, 0, F - dF])
    global MAXFORCE
    MAXFORCE = max(MAXFORCE, (F + dF) / 4)
    print("Force vectors", force_vec, less_vec)
    print("Max force", MAXFORCE)
    if idx == 0:
        return np.array([force_vec, less_vec, less_vec, force_vec])
    elif idx == 1:
        return np.array([force_vec, force_vec, less_vec, less_vec])


def orient(target):
    quat = drone.get_quaternion()
    orientation = quaternion_to_euler(*quat)
    forceX = calc_stuff(orientation, target, 0)
#    forceY = calc_stuff(orientation, target, 1)
    return forceX
#    return (forceX + forceY) / 2


def calc_force():
    global mode
    mg = mass * world.get_gravity()[2]
#    print("mg:", mg)
    az = 12 # vertical acceleration
    if mode == ord('w'):
        return orient(np.array([0, 0, -tilt]))
    elif mode == ord('a'):
        return orient(np.array([0, -tilt, 0]))
    elif mode == ord('s'):
        return orient(np.array([0, 0, tilt]))
    elif mode == ord('d'):
        return orient(np.array([0, tilt, 0]))
    elif mode == UP:
        return np.array([np.array([0, 0, mg + mass*az])] * 4)
    elif mode == DOWN:
        return np.array([np.array([0, 0, -mass*az + mg])] * 4)
    elif mode == ord(' '):
        return stabilize()


    return np.zeros((4,3))


def controlmapping() -> None:
    global drone
#    print("Time:", world.get_world_time())
    force = calc_force()
    r = [np.array([mr, mr, 0]), np.array([mr, -mr, 0]), np.array([-mr, -mr, 0]), np.array([-mr, mr, 0])]
    r = np.array(r)
    rotation = drone.get_rotation_matrix()
    F = force.transpose()
    F = rotation @ F
    F = F.transpose()
#    print("Rotated F", F)


    # https://github.com/leggedrobotics/raisimLib/blob/master/include/raisim/object/singleBodies/SingleBodyObject.hpp
    for i in range(len(r)):
        drone.set_external_force(1, r[i], F[i] / 4)

#    drone.set_external_torque(1, np.cross(r, F))


if __name__ == '__main__':
    # create raisim world
    world = raisim.World()
    world.set_time_step(time_step)
    world.set_erp(world.get_time_step() * 0.1, world.get_time_step() * 0.1)

    vis = raisim.OgreVis.get()
    setup_vis(world, vis)

    # create raisim objects
#    world.set_gravity(np.array([0, 0, 0]))
    ground = world.add_ground()
    drone = world.add_box(x=width, y=width, z=height, mass=mass)
    drone.set_position(np.array([0, 0, 20]))
#    drone.set_orientation(.8, -0.2, -.2, 0)

    # create visualizer objects
    vis.create_graphical_object(ground, dimension=50, name="floor", material="default")
    vis.set_keyboard_callback(keymapping)
    vis.set_control_callback(controlmapping)
    drone_graphics = vis.create_graphical_object(drone, name="drone", material="blue")
    vis.select(drone_graphics[0])
    vis.get_camera_man().set_yaw_pitch_dist(0, -np.pi / 4., 20)


    # run the app
    vis.run()

    # terminate
    vis.close_app()
