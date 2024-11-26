def min_s(arr):
    if arr:
        return min(arr)
    return 0

def can_move(y, x):
    return 0 <= y < n and 0 <= x < n 
dys = [0, -1]
dxs = [1, 0]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for y in range(n):
    for x in reversed(range(n)):
        arr[y][x] += min_s(
            [arr[y + dy][x + dx] for dy, dx in zip(dys, dxs) if can_move(y + dy, x + dx)]
        )

print(arr[-1][0])