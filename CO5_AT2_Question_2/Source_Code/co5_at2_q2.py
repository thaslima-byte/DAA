# K-Colorability using Backtracking

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

n = len(graph)
k = 3

colors = [0] * n


def is_safe(vertex, color):
    for i in range(n):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True


def graph_coloring(vertex):
    if vertex == n:
        return True

    for color in range(1, k + 1):

        if is_safe(vertex, color):
            colors[vertex] = color

            if graph_coloring(vertex + 1):
                return True

            # Backtrack
            colors[vertex] = 0

    return False


if graph_coloring(0):
    print("Graph can be colored with", k, "colors")
    print("Color Assignment:", colors)
else:
    print("Graph cannot be colored")