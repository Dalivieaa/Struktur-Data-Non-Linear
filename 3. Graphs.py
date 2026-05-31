# 3. Graphs

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print("adjacency list:")
for node in graph:
    print(node, "->", graph[node])