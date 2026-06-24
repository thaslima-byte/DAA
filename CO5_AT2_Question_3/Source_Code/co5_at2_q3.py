# Generate all subsets in Lexicographic Order using Backtracking

elements = [1, 2, 3]

# Sort elements to ensure lexicographic order
elements.sort()

current_subset = []


def generate_subsets(start):

    # Print current subset
    print(current_subset)

    # Generate remaining subsets
    for i in range(start, len(elements)):

        # Include current element
        current_subset.append(elements[i])

        # Recursive call
        generate_subsets(i + 1)

        # Backtrack
        current_subset.pop()


print("Subsets in Lexicographic Order:")
generate_subsets(0)