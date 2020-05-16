#!/usr/bin/env python
# UR RETARDED AND PROLLY GONNA FORGET THIS, BUT USE THE TERMINAL IN MOBA X TERM, NOT JUST THE X SERVER
import os
import numpy as np
import raisimpy as raisim

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
offset = 0.5
height = 7
width = 6
radius = 0.5


def normalize(array):
    return np.asarray(array) / np.linalg.norm(array)


def act(plate, action) -> None:
    force = np.array([0, 0, 0])
    if action == LEFT:
        force[0] = -100
    elif action == RIGHT:
        force[0] = 100
    elif action == UP:
        force[1] = 100
    elif action == DOWN:
        force[1] = -100
    plate.set_external_force(1, force)


def create_env(time_step=0.01):
    # create raisim world
    world = raisim.World()
    world.set_time_step(time_step)
    world.set_erp(world.get_time_step() * 0.1, world.get_time_step() * 0.1)

    # create raisim objects
    ground = world.add_ground()
    plate = world.add_box(x=width, y=width, z=offset, mass=5)
    cylinder = world.add_cylinder(radius=radius, height=height, mass=1)
    plate.set_position(0, 0, offset / 2)
    cylinder.set_position(0, 0, offset + height / 2)
    cylinder.set_orientation(1, 0, 0, 0)

    return world, plate, cylinder
