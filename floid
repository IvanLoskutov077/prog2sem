INF = float('inf')


def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Пример графа в виде матрицы смежности
graph = [
    [0, 4, 0, 0, 0, 0],
    [4, 0, 8, 0, 0, 0],
    [0, 8, 0, 7, 0, 4],
    [0, 0, 7, 0, 9, 14],
    [0, 0, 0, 9, 0, 10],
    [0, 0, 4, 14, 10, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(*row)
