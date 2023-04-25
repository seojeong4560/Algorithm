from collections import deque
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    deq = deque()
    tmp_arr = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 2:
                deq.append((i, j))

    while deq:
        x, y = deq.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < N and 0 <= ny < M and tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                deq.append((nx, ny))

    global dap 
    cntt = 0
    for i in range(N):
        cntt += tmp_arr[i].count(0)

    dap = max(dap, cntt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(cnt + 1)
                arr[i][j] = 0

# 세로 N 가로 M
N, M = map(int, input().split())

# 지도 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)]

# 구하고자 하는 답, 안전 영역의 최대 크기 
dap = 0

makeWall(0)

print(dap)