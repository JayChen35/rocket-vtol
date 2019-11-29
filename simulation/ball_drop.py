import raisimpy as raisim
import os

world = raisim.World()
ball = world.add_sphere(radius=1, mass=1)
ground = world.add_ground()

ball.set_position(0, 0, 20)
gravity = world.get_gravity()
print("Gravity is", gravity)
print(ball.get_position())
print("Initial total energy is", ball.get_energy(gravity))

total = 0
time_step = 0.002

while ball.get_position()[2] > ball.get_radius():
#    print("Vertical position of ball:", ball.get_position()[2])
#    print("Vertical velocity of ball", ball.get_linear_velocity()[2])
    world.set_time_step(time_step)
    world.integrate()
    total += time_step
#    time_step += 0.002

print("Time:", total)
vel = abs(ball.get_linear_velocity()[2])
print("Calculcated velocity (with kinematics)", (2 * abs(gravity[2]) * 20) ** (1/2))
print("Calculated velocity (also with kinematics)", gravity[2] * total)
print("Measured velocity", vel)
print("Calculated KE (from velocity)", vel ** 2 / 2)
print("Measured KE", ball.get_kinetic_energy())
print("Measured PE", ball.get_potential_energy(gravity))
print("Final total energy is", ball.get_energy(gravity))
