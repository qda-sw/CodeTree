from collections import Counter

def dfs(cur):
    for _next in graph[cur]:
        if visited[_next]:
            continue
        visited[_next] = True
        dfs(_next)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    _from, _to = map(lambda x: int(x)-1, input().split())
    graph[_from].append(_to)
    graph[_to].append(_from)

visited = [False]*n

dfs(0)
print(sum([1 for e in visited if e]) - 1)