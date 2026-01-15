import matplotlib.pyplot as plt

# ======================
# Q-learning (Phase 2)
# ======================
episodes_q = [
    500, 1000, 1500, 2000, 2500, 3000, 3500, 4000,
    4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000
]

success_q = [
    2.6, 4.2, 4.2, 7.0, 7.2, 5.6, 12.6, 12.4,
    11.8, 10.6, 11.6, 14.2, 15.2, 13.2, 12.0, 13.8
]

# ======================
# PPO (Phase 2)
# ======================
episodes_ppo = [
    500, 1000, 1500, 2000, 2500, 3000, 3500, 4000,
    4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000
]

success_ppo = [
    30.0, 28.8, 33.2, 25.2, 21.0, 23.2, 26.0, 20.0,
    19.2, 19.2, 19.6, 23.2, 23.6, 22.2, 19.6, 23.8
]

# ======================
# Plot
# ======================
plt.figure(figsize=(8, 5))
plt.plot(episodes_q, success_q, marker='o', label='Q-learning')
plt.plot(episodes_ppo, success_ppo, marker='s', label='PPO')

plt.xlabel("Episode")
plt.ylabel("Success Rate (%)")
plt.title("Episode vs Success Rate (MiniGrid DoorKey Enemy)")
plt.legend()
plt.grid(True)

plt.show()
