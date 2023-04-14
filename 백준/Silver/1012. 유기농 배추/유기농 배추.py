from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    deq = deque()
    deq.append((x,y))
    visited[x][y] = 1

    while deq:
        x, y = deq.pop()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                deq.append((nx, ny))


T = int(input())

for tc in range(1, T+1):
    # M 가로 N 세로 K 배추가 심어져 있는 위치 개수
    m, n, k = map(int, input().split())

    arr = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    # 배추 흰지렁의 마리 수
    dap = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(i, j)
                dap += 1

    print(dap)