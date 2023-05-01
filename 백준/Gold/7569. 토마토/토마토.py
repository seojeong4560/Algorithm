import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 3차원 bfs
def bfs():
    while deq:
        # z, x, y 순서
        z, x, y = deq.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                # z, x, y 순서
                if data[nz][nx][ny] == 0:
                    data[nz][nx][ny] = data[z][x][y] + 1
                    deq.append((nz, nx, ny))

# M 상자 가로 N 상자 세로 H 상자 수
M, N, H = map(int, input().split())

data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

deq = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            # z, x, y 순서
            if data[i][j][k] == 1:
                # z, x, y 순서
                deq.append((i, j, k))

bfs()

flag = 0
dap = -2

for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 0:
                flag = 1
            dap = max(dap, data[i][j][k])


# 토마토가 모두 익지는 못하는 상황이면 -1 출력
if flag == 1:
    print(-1)
# 저장될 때 부터 모든 토마토가 익어있는 상태면 0 출력
elif dap == -1:
    print(0)
else:
    print(dap-1)
                