dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

def can_move(y, x):
    return 0 <= y < n and 0 <= x < n and arr[y][x] == 1

def find_village(y, x):
    if not can_move(y, x):
        return 0
    arr[y][x] = 0
    population = 1
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        population += find_village(ny, nx)
    return population

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = []
for r in range(n):
    for c in range(n):
        temp = find_village(r, c)
        if temp:
            result.append(temp)
print(len(result))
print(*sorted(result), sep='\n')