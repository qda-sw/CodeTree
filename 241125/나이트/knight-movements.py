from collections import deque


def bfs():
    def can_move(y, x):
        return 0 <= y < n and 0 <= x < n and not (y, x) in visited

    dys = [1, 2, 2, 1, -1, -2, -2, -1]
    dxs = [2, 1, -1, -2, -2, -1, 1, 2]
    visited = set()
    queue = deque()
    queue.append((r1-1, c1-1, 0))
    visited.add((r1-1, c1-1))
    while queue:
        y, x, depth = queue.popleft()
        if y == r2-1 and x == c2-1:
            return depth
        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_move(ny, nx):
                visited.add((ny, nx))
                queue.append((ny, nx, depth+1))
    return -1
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
print(bfs())