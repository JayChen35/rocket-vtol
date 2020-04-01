import os
import raisimpy as raisim
import numpy as np
np.set_printoptions(precision=2)


offset = 0.5
height = 7
width = 3
radius = 0.5

world = raisim.World()
plate = world.add_box(x=width, y=width, z=offset, mass=5)
cylinder = world.add_cylinder(radius=radius, height=height, mass=1)
#ball = world.add_sphere(radius=1, mass=1)
ground = world.add_ground()

print("Before setting position:", plate.get_position())
print("Ground position", ground.get_position())
plate.set_position(0, 0, offset / 2)
cylinder.set_position(0, 0, offset + height / 2)
cylinder.set_orientation(1, 0, 0, 0)
gravity = world.get_gravity()
print("Orientation:", cylinder.get_quaternion())
print("Gravity is", gravity)
print("Starting position:", plate.get_position())
print("Starting energy:", plate.get_energy(gravity))
print(cylinder.get_position())
print("Initial cylinder energy is", cylinder.get_energy(gravity))
#print(1/0)
plate.set_external_force(1, np.array([100, 0, 0]))
total = 0
time_step = 1

for i in range(100):
#    print("Position of plate:", plate.get_position())
#    print("Position of cylinder:", cylinder.get_position())
    world.set_time_step(time_step)
    world.integrate()
    total += time_step
#    time_step += 0.002


print("Time:", total)
print("Final position:", plate.get_position())
print("Final velocity:", plate.get_linear_velocity())
print("Final energy:", plate.get_energy(gravity))
print("Final cylinder position", cylinder.get_position())
print("Final cylinder energy", cylinder.get_energy(gravity))
print("Final orientation:", cylinder.get_quaternion())
