n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


cnt = 0
def dfs(index):
    global cnt
    for i in graph[index]:
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i)


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited[1] = 1
dfs(1)

print(cnt)