import gym

from stable_baselines3 import DQN

env = gym.make("CartPole-v0")
# https://gym.openai.com/envs/CartPole-v1/
# A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track.
# The system is controlled by applying a force of +1 or -1 to the cart.
# The pendulum starts upright, and the goal is to prevent it from falling over.
# A reward of +1 is provided for every timestep that the pole remains upright.
# The episode ends when the pole is more than 15 degrees from vertical,
# or the cart moves more than 2.4 units from the center.

train_time = 0 #100000

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=train_time, log_interval=4)
model.save("dqn_cartpole2")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_cartpole2")

obs = env.reset()
ep_count = 0
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        print(f'Episode {ep_count}')
        ep_count += 1
        obs = env.reset()
