import matplotlib.pyplot as plt

# ======================
# Episodes
# ======================
episodes = [
    500, 1000, 1500, 2000, 2500, 3000, 3500, 4000,
    4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000
]

# ======================
# avg_reward(last500)
# ======================

# v1
reward_v1 = [
     0.047,  0.035,  0.078, -0.046,
    -0.128, -0.113, -0.058, -0.146,
    -0.156, -0.154, -0.176, -0.125,
    -0.117, -0.145, -0.169, -0.106
]

# v2
reward_v2 = [
     0.003,  0.001,  0.012, -0.012,
    -0.057, -0.014, -0.078, -0.046,
    -0.091, -0.142, -0.102, -0.071,
    -0.044, -0.020, -0.074, -0.091
]

# ======================
# Plot
# ======================
plt.figure(figsize=(8, 5))

plt.plot(episodes, reward_v1, marker='o', label='v1')
plt.plot(episodes, reward_v2, marker='s', label='v2')

plt.xlabel("Episode")
plt.ylabel("Average Reward (last 500)")
plt.title("PPO — Average Reward vs Episode")
plt.legend()
plt.grid(True)

plt.show()
