from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    arr[x][y] = 2

    while queue:
        x, y = queue.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                queue.append((nx, ny))


# M: 세로 N: 가로
M, N = map(int, input().split())

# 입력값이 항상 띄어쓰기 인지 확인, 이거 때매 틀림
arr = [list(map(int, input())) for _ in range(M)]

for i in range(N):
    if arr[0][i] == 0:
        bfs(0, i)

flag = 0
for i in range(N):
    if arr[M-1][i] == 2:
        flag = 1

if flag:
    print('YES')
else:
    print('NO')