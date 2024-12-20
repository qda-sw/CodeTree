def can_move(y, x):
    return 0 <= y < n and 0 <= x < m and arr[y][x] == 1

dy = [0, 1]
dx = [1, 0]


def dfs(y, x):
    for _dy, _dx in zip(dy, dx):
        next_y = y + _dy
        next_x = x + _dx
        if not can_move(next_y, next_x):
            continue
        arr[next_y][next_x] = 0
        dfs(next_y, next_x)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dfs(0, 0)
print(1 if arr[n-1][m-1] == 0 else 0)