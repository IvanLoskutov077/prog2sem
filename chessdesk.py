from collections import deque


def min_steps_to_reach_target(n, i, j, x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = deque([(i, j, 0)])
    visited[i][j] = True

    while queue:
        curr_x, curr_y, steps = queue.popleft()

        if curr_x == x and curr_y == y:
            return steps

        for k in range(8):
            next_x = curr_x + dx[k]
            next_y = curr_y + dy[k]

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, steps + 1))

    return -1  # Если не удалось достичь целевой клетки

# Пример
n = 8
i, j = 0, 0
x, y = 2, 2
if i > n or j > n or x > n or y > n:
    print("Точка за пределами доски")
    raise SystemExit

min_steps = min_steps_to_reach_target(n, i, j, x, y)
print(f"Минимальное количество шагов: {min_steps}")
