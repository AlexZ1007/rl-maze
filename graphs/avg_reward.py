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
    -0.469, -0.422, -0.417, -0.397, -0.397, -0.357,
    -0.314, -0.290, -0.302, -0.322, -0.307, -0.243,
    -0.276, -0.285, -0.324, -0.313
]

# v2
reward_v2 = [
    -0.220, -0.238, -0.202, -0.214, -0.217, -0.190,
    -0.189, -0.163, -0.189, -0.160, -0.194, -0.160,
    -0.150, -0.152, -0.169, -0.177
]

# v3
reward_v3 = [
    -0.255, -0.226, -0.240, -0.218, -0.219, -0.188,
    -0.161, -0.183, -0.176, -0.158, -0.178, -0.152,
    -0.135, -0.188, -0.173, -0.170
]

# ======================
# Plot
# ======================
plt.figure(figsize=(8, 5))

plt.plot(episodes, reward_v1, marker='o', label='v1')
plt.plot(episodes, reward_v2, marker='s', label='v2')
plt.plot(episodes, reward_v3, marker='^', label='v3')

plt.xlabel("Episode")
plt.ylabel("Average Reward (last 500)")
plt.title("Q-learning Phase 2 — Average Reward vs Episode")
plt.legend()
plt.grid(True)

plt.show()
