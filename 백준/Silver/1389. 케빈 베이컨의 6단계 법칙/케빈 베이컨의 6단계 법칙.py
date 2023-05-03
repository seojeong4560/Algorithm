from collections import deque

# bfs 탐색
def bfs(v):
    deq = deque()
    deq.append(v)
    visited[v] = 1

    while deq:
        target = deq.popleft()

        # 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색
        for i in graph[target]:
            if not visited[i]:
                # 탐색하기 위한 횟수를 체크한다. 
                visited[i] = visited[target] + 1
                deq.append(i)

# 유저의 수 N 친구 관계의 M
N, M = map(int, input().split())

# M개의 줄에 친구 관계
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 케빈 베이컨의 수를 담는 리스트
dap = []

# 반복문을 통해 모든 친구를 탐색
for i in range(1, N+1):
    visited = [0] * (N+1)
    bfs(i)
    dap.append(sum(visited))

# 가장 작은 케빈 베이컨의 수를 가지고 있는 사람의 인덱스 + 1을 해주어 출력한다.
print(dap.index(min(dap)) + 1)