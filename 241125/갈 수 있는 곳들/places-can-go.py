from collections import deque

def can_move(y, x):
    return 0 <= y < n and 0 <= x < n and grid[y][x] == 0
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]
def bfs(y, x):
    if grid[y][x] == 1:
        return 0
    queue = deque()
    grid[y][x] = 1
    queue.append((y, x))
    result = 1 if grid[y][x] == 0 else 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if not can_move(ny, nx):
                continue
            grid[ny][nx] = 1
            queue.append((ny, nx))
            result += 1
    return result
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_points = [(y-1, x-1) for y, x in [map(int, input().split()) for _ in range(k)]]

result = 0
for y, x in start_points:
    result += bfs(y, x)
print(result)