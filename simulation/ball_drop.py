import raisimpy as raisim
import os

world = raisim.World()
ball = world.add_sphere(radius=1, mass=1)
ground = world.add_ground()

ball.set_position(0, 0, 20)
print(ball.get_position())

time_step = 0

while ball.get_position()[2] > ball.get_radius():
    print("Vertical position of ball:", ball.get_position()[2])
    print("Vertical velocity of ball", ball.get_linear_velocity()[2])
    world.set_time_step(time_step)
    world.integrate()
    time_step += 0.002

print(time_step)