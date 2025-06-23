import random

streak_count = 0  # Count how many streaks of 6+ occur
total_experiments = 10000  # Number of simulations

for _ in range(total_experiments):
    flips = [random.choice(['H', 'T']) for _ in range(100)]

    # Check for streaks of 6
    for i in range(len(flips) - 5):
        if all(flips[i] == flips[i + j] for j in range(6)):
            streak_count += 1
            break  # Only count one streak per experiment

# Display the percentage of streaks
percentage = (streak_count / total_experiments) * 100
print(f"Chance of a streak of 6 in 100 flips: {percentage:.2f}%")
