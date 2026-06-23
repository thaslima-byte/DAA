# Clique Partitioning using Backtracking

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

n = len(graph)

cliques = []


def can_add(vertex, clique):
    for v in clique:
        if graph[vertex][v] == 0:
            return False
    return True


def partition(vertex):
    if vertex == n:
        return True

    # Try existing cliques
    for clique in cliques:
        if can_add(vertex, clique):
            clique.append(vertex)

            if partition(vertex + 1):
                return True

            clique.pop()  # Backtrack

    # Create new clique
    cliques.append([vertex])

    if partition(vertex + 1):
        return True

    cliques.pop()  # Backtrack

    return False


partition(0)

print("Clique Partitions:")

for i, clique in enumerate(cliques):
    print(f"Clique {i + 1}:", clique)

print("\nAnalysis:")
print("- Backtracking explores partitions.")
print("- Pruning avoids invalid clique formations.")
print("- Clique Partitioning is NP-Hard.")