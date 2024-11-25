from collections import deque


def bfs():
    def can_move(y, x):
        return 0 <= y < n and 0 <= x < n and not visited[y][x]

    dys = [1, 2, 2, 1, -1, -2, -2, -1]
    dxs = [2, 1, -1, -2, -2, -1, 1, 2]
    visited = [[False for _ in range(n)] for _ in range(n)]
    steps = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((r1-1, c1-1))
    visited[r1-1][c1-1] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_move(ny, nx):
                visited[ny][nx] = True
                steps[ny][nx] = steps[y][x] + 1
                queue.append((ny, nx))
    return steps[r2-1][c2-1] if visited[r2-1][c2-1] else -1
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
print(bfs())