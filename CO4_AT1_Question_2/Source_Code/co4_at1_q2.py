# Maximum Number of Non-Overlapping Segments
# Greedy Approach

def max_non_overlapping_segments(segments):
    
    # Sort segments based on ending time
    segments.sort(key=lambda x: x[1])

    count = 0
    last_end = -1

    selected_segments = []

    for start, end in segments:
        if start >= last_end:
            count += 1
            last_end = end
            selected_segments.append((start, end))

    return count, selected_segments


# Driver Code
n = 3

segments = [(1, 2), (2, 3), (3, 4)]

count, selected = max_non_overlapping_segments(segments)

print("Segments:")
for seg in segments:
    print(seg)

print("\nSelected Non-Overlapping Segments:")
for seg in selected:
    print(seg)

print("\nMax Segments =", count)