import gymnasium as gym
import numpy as np
from stable_baselines3 import SAC, TD3

env = gym.make("CarRacing-v3", render_mode="human", lap_complete_percent=0.95, domain_randomize=False, continuous=True, max_episode_steps=1000,)
model = SAC("MlpPolicy", env, verbose=1, gradient_steps=1, train_freq=1, learning_rate=0.00003, batch_size=256, tensorboard_log="./a2c_cartpole_tensorboard/")
model.learn(total_timesteps=100000, log_interval=4, progress_bar=True)
model.save("sac_carracing_model")
# model = SAC.load("sac_carracing_model", env=env)

total_reward = 0
obs, info = env.reset()
terminated, truncated = False, False
while not (terminated or truncated):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    env.render()

print("Episode finished. Total reward:", total_reward)
