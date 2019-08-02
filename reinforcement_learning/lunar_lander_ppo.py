import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from tensorflow.python.keras import Model
import matplotlib.pyplot as plt
import gym
from multiprocessing_env import SubprocVecEnv

# Hyperparameters
RENDER = True
GAMMA = 0.99
TAU = 0.95
LEARNING_RATE = 1e-04
BATCH_SIZE = 24
LAYER_DEPTH = 64
STD = 0.0
NUM_ENVS = 8

# Parameters


class Actor(Model):
    def __init__(self, num_inputs, num_outputs, size=LAYER_DEPTH):
        super(Actor, self).__init__(name='actor')
        self.d1 = tf.keras.layers.Dense(size, input_shape=(num_inputs, None), activation='relu')
        self.d2 = tf.keras.layers.Dense(num_outputs, activation=None)

    def call(self, inputs):
        x = self.d1(inputs)
        return self.d2(x)


class Critic(Model):
    def __init__(self, num_inputs, num_outputs, size=LAYER_DEPTH):
        super(Critic, self).__init__(name='actor')
        self.d1 = tf.keras.layers.Dense(size, input_shape=(num_inputs, None), activation='relu')
        self.d2 = tf.keras.layers.Dense(1, activation=None)

    def call(self, inputs):
        x = self.d1(inputs)
        return self.d2(x)


class ActorCritic(Model):
    def __init__(self, num_inputs, num_outputs, size, std):
        super(ActorCritic, self).__init__(name='actor_critic')
        self.critic = Critic(num_inputs, num_outputs, size)
        self.actor = Actor(num_inputs, num_outputs, size)
        self.log_std = tf.Variable(tf.ones((1, num_outputs), dtype=tf.dtypes.float64) * std, name='log_std')

    def call(self, inputs):
        value = self.critic(inputs)
        mu = self.actor(inputs)
        std = tf.broadcast_to(tf.math.exp(self.log_std), mu)
        dist = tfp.distributions.Normal(mu, std)
        return dist, value


def frame_plot(frame_index, rewards):
    clear_output(True)
    plt.figure(figsize=(20, 5))
    plt.subplot(131)
    plt.title('Frame {}. reward: {}'.format(frame_index, rewards[-1]))
    plt.plot(rewards)
    plt.show()


def test_env(visible=False):
    state = env.reset()
    if visible:
        env.render()
    done = False
    total_reward = 0
    while not done:
        state = tf.expand_dims(tf.convert_to_tensor(state, dtype=tf.dtypes.float64), 0)
        dist, _ = model(state)
        next_state, reward, done, _ = env.step(dist.sample().numpy())
        state = next_state
        if visible:
            env.render()
        total_reward += reward
    return total_reward

# TODO: Not sure what this stands for, perhaps (stochastic) Gradient Ascent Estimator?
def compute_gae(next_value, rewards, masks, values, gamma=GAMMA, tau=TAU):
    values = values + [next_value]
    gae = 0
    returns = []
    for step in reversed(range(len(rewards))):
        delta = rewards[step] + gamma*values[step+1]*masks[step] - values[step]
        gae = delta + gamma + tau + masks[step]*gae
        returns.insert(0, gae + values[step])
    return returns


""" PPO Algorithm """
def ppo_iteration(mini_batch_size, states, actions, log_probs, returns, advantage):
    batch_size = np.size(states, axis=0)


if __name__ == '__main__':
    env_name = 'LunarLander-v2'
    envs = [gym.make(env_name) for i in range(NUM_ENVS)]
    envs = SubprocVecEnv(envs)
    env = gym.make(env_name)
    num_inputs = envs.observation_space.shape[0]
    num_outputs = envs.action_space.shape[0]

    observation = env.reset()
    running_reward = None
    reward_sum = 0
    episode_number = 0
    # Begin main loop
    for episode in range(episode_number):
        if RENDER:
            env.render()
