# Constraint-Based Pattern Matching using Backtracking

def match_pattern(text, pattern, pos=0):
    # Base Case
    if len(pattern) == 0:
        return True

    # If pattern is longer than remaining text
    if len(text) < len(pattern):
        return False

    # Try all possible alignments
    for i in range(pos, len(text) - len(pattern) + 1):

        valid = True

        # Check matching constraints
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                valid = False
                break  # Pruning

        if valid:
            return True

    return False


# Driver Code
text = "ABCDABCABCD"
pattern = "ABC"

print("Text:", text)
print("Pattern:", pattern)

if match_pattern(text, pattern):
    print("Pattern Match Found")
else:
    print("Pattern Not Found")

print("\nAnalysis:")
print("- Backtracking explores alignments.")
print("- Pruning reduces unnecessary comparisons.")
print("- Worst-case complexity is exponential.")