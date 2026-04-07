from env import SimpleEnv

env = SimpleEnv()
state = env.reset()

total_reward = 0

for _ in range(10):
    state, reward, done = env.step("work")
    total_reward += reward
    if done:
        break

print("Score:", total_reward)