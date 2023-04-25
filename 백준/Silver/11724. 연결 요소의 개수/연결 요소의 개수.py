import sys
sys.setrecursionlimit(5000)

def dfs(start, depth):
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [0] * (N + 1)
# 그래프 개수 저장
dap = 0

# 1 ~ N 번 노드를 각각 돌면서
for i in range(1, N+1):
    if not visited[i]:
        # 만약 해당 정점이 연결된 그래프가 없다면
        if not graph[i]:
            dap += 1
            visited[i] = 1
        else:
            dfs(i, 0)
            dap += 1

print(dap)