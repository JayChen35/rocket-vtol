import raisimpy as raisim

world = raisim.World()
anymal = world.add_articulated_system("../../raisimpy/examples/rsc/ANYmal/anymal.urdf")
ball = world.add_sphere(radius=1, mass=1)
ground = world.add_ground()

world.set_time_step(0.002)
world.integrate()
print(anymal.get_frame_world_position(1))