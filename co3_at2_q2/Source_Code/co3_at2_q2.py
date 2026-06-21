import random
import time

# Quick Sort using Random Pivot
def quick_sort(scores):
    if len(scores) <= 1:
        return scores

    # Random pivot selection for improved performance
    pivot = random.choice(scores)

    left = [x for x in scores if x[1] > pivot[1]]
    middle = [x for x in scores if x[1] == pivot[1]]
    right = [x for x in scores if x[1] < pivot[1]]

    return quick_sort(left) + middle + quick_sort(right)


# Live Sports Score Data
players = [
    ("Player A", 95),
    ("Player B", 88),
    ("Player C", 76),
    ("Player D", 92),
    ("Player E", 88),
    ("Player F", 99),
    ("Player G", 81),
    ("Player H", 95)
]

print("LIVE SPORTS SCOREBOARD")
print("-------------------------")

print("\nOriginal Rankings:")
for player in players:
    print(player)

# Measure execution time
start = time.perf_counter()

sorted_players = quick_sort(players)

end = time.perf_counter()

print("\nUpdated Rankings (Highest Score First):")
rank = 1
for player in sorted_players:
    print(f"Rank {rank}: {player[0]} - {player[1]} points")
    rank += 1

print("\nExecution Time:", end - start, "seconds")

print("\nAnalysis:")
print("- Random pivot selection improves efficiency.")
print("- Divide and Conquer technique is used.")
print("- Worst-case complexity O(n²) is minimized.")
print("- Average-case complexity remains O(n log n).")