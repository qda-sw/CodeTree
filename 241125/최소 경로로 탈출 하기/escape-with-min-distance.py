from collections import deque

def can_move(y, x):
    return 0 <= y < n and 0 <= x < m and arr[y][x] == 1
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]
def bfs():
    queue = deque()
    arr[0][0] = 0
    queue.append((0, 0))
    depth = 0
    while queue:
        y, x = queue.popleft()
        if y == n-1 and x == m-1:
            return arr[y][x]
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_move(ny, nx):
                arr[ny][nx] = arr[y][x] + 1
                queue.append((ny, nx))
    return -1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

print(bfs())