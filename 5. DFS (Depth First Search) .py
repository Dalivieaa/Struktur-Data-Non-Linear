# 5. DFS (Depth First Search) 
# algoritma pencarian yang menjelajahi node secara mendalam sebelum melanjutkan ke node lain. 
# Selesai praktikum semester 

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
 
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("hasil DFS:")
dfs(graph, "A")
print()
