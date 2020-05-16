from cartpole_env import create_env, act
from ai import RandomAI

time_step = 0.1
total = 0
world, plate, cylinder = create_env(time_step)
player = RandomAI()
for i in range(1000000):
    state = player.process_state(world, plate, cylinder)
    action = player.act(state)
    act(plate, action)
    world.set_time_step(time_step)
    world.integrate()
    total += time_step

print("Score:", total)
print(player.process_state(world, plate, cylinder))
