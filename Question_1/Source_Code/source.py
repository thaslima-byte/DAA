import time

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # <= maintains stability
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2][0]

    left = [x for x in arr if x[0] < pivot]
    middle = [x for x in arr if x[0] == pivot]
    right = [x for x in arr if x[0] > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Dataset with duplicate values
data = [
    (5, 'A'),
    (3, 'B'),
    (5, 'C'),
    (2, 'D'),
    (3, 'E'),
    (8, 'F'),
    (5, 'G'),
    (2, 'H')
]

print("Original Data:")
print(data)

# Merge Sort Timing
start = time.perf_counter()
merge_sorted = merge_sort(data.copy())
end = time.perf_counter()

merge_time = end - start

print("\nAfter Merge Sort:")
print(merge_sorted)
print("Execution Time:", merge_time, "seconds")


# Quick Sort Timing
start = time.perf_counter()
quick_sorted = quick_sort(data.copy())
end = time.perf_counter()

quick_time = end - start

print("\nAfter Quick Sort:")
print(quick_sorted)
print("Execution Time:", quick_time, "seconds")