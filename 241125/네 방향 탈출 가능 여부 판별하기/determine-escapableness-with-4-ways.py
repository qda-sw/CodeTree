from collections import deque

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

def can_move(y, x):
    return 0 <= y < n and 0 <= x < m and arr[y][x] == 1

queue = deque()
def bfs():
    while queue:
        y, x = queue.popleft()
        arr[y][x] = 0
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if not can_move(ny, nx):
                continue
            queue.append((ny, nx))

    

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue.append((0, 0))
bfs()
print(1 if arr[n-1][m-1] == 0 else 0)