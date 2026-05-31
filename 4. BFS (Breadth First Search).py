#4. BFS (Breadth First Search) 

# algoritma pencarian yang menjelajahi semua node pada level yang sama sebelum melanjutkan ke level berikutnya
# Menggunakan struktur data antrian (queue) untuk menyimpan node yang akan dijelajahi selanjutnya.

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
 
def bfs(graph, start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

print("hasil BFS:")
bfs(graph, "A")
print()