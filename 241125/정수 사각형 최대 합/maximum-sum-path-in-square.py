def can_move(y, x):
    return 0 <= y < n and 0 <= x < n

dys = [-1, 0]
dxs = [0, -1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for y in range(n):
    for x in range(n):
        arr[y][x] += max(
            [arr[y + dy][x + dx] for dy, dx in zip(dys, dxs) if can_move(y+dy, x+dx)] + [0]
        )
print(arr[-1][-1])