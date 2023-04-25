import sys
sys.setrecursionlimit(3000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            arr[nx][ny] = 2
            dfs(nx, ny)


# M: 세로 N: 가로
M, N = map(int, input().split())

# 입력값이 항상 띄어쓰기 인지 확인, 이거 때매 틀림
arr = [list(map(int, input())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

for i in range(N):
    if arr[0][i] == 0 and visited[0][i] == 0:
        visited[0][i] = 1
        dfs(0, i)

dap = 0
for i in range(N):
    if arr[M-1][i] == 2:
        dap = 'YES'

if dap == 'YES':
    print(dap)
else:
    print('NO')