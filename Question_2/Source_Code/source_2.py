import random
import time

# Quick Sort using first element as pivot
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # First element as pivot

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Nearly Sorted Dataset
nearly_sorted = list(range(1, 1001))

# Introduce slight disorder
nearly_sorted[500], nearly_sorted[501] = nearly_sorted[501], nearly_sorted[500]

# Random Dataset
random_data = list(range(1, 1001))
random.shuffle(random_data)

# Measure execution time for Nearly Sorted Dataset
start = time.perf_counter()
sorted_nearly = quick_sort(nearly_sorted.copy())
end = time.perf_counter()

nearly_time = end - start

# Measure execution time for Random Dataset
start = time.perf_counter()
sorted_random = quick_sort(random_data.copy())
end = time.perf_counter()

random_time = end - start

# Display Results
print("QUICK SORT PERFORMANCE ANALYSIS")
print("--------------------------------")

print("\nDataset Size:", len(nearly_sorted))

print("\nExecution Time for Nearly Sorted Dataset:")
print(nearly_time, "seconds")

print("\nExecution Time for Random Dataset:")
print(random_time, "seconds")

print("\nPerformance Comparison:")
if nearly_time > random_time:
    print("Quick Sort performed slower on nearly sorted data.")
else:
    print("Quick Sort performed efficiently on both datasets.")

print("\nAnalysis:")
print("Using the first element as pivot can degrade performance")
print("for nearly sorted datasets, leading to O(n^2) complexity.")
print("Randomized or Median-of-Three pivot selection can improve efficiency.")