import time

# Merge function
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Sort by departure time
        # <= ensures stability
        if left[i][2] <= right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Merge Sort Function
def merge_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    mid = len(bookings) // 2

    left = merge_sort(bookings[:mid])
    right = merge_sort(bookings[mid:])

    return merge(left, right)


# Flight Booking Data
bookings = [
    ("P101", "High", "09:30"),
    ("P102", "Normal", "08:45"),
    ("P103", "High", "09:30"),
    ("P104", "Normal", "07:50"),
    ("P105", "VIP", "08:45"),
    ("P106", "Normal", "10:15")
]

print("Original Flight Bookings:")
for booking in bookings:
    print(booking)

# Measure execution time
start = time.perf_counter()

sorted_bookings = merge_sort(bookings)

end = time.perf_counter()

print("\nSorted Flight Bookings (by Departure Time):")
for booking in sorted_bookings:
    print(booking)

print("\nExecution Time:", end - start, "seconds")