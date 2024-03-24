class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, vertex):
        self.heap.append(vertex)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < len(self.heap) and self.heap[left][0] < self.heap[i][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)


def dijkstra_with_min_heap(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = MinHeap()
    pq.insert((0, start))

    while len(pq.heap) > 0:
        d, u = pq.extract_min()

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.insert((dist[v], v))

    return dist


# Пример использования
graph = {
    0: [(1, 5), (2, 3)],
    1: [(2, 2), (3, 6)],
    2: [(3, 7)],
    3: []
}

start_vertex = 0
shortest_distances = dijkstra_with_min_heap(graph, start_vertex)

print("Кратчайшие расстояния от стартовой точки до каждой вершины:")
for i, dist in enumerate(shortest_distances):
    print(f"До вершины {i}: {dist}")