from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    global sheep
    global wolf

    deq = deque()
    deq.append((i, j))

    visited[i][j] = 1

    while deq:
        i, j = deq.popleft()

        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]
            if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj] and arr[ni][nj] != "#":
                visited[ni][nj] = 1
                if arr[ni][nj] == "v":
                    wolf += 1
                if arr[ni][nj] == "o":
                    sheep += 1

                deq.append((ni, nj)) 

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

dap_sheep = 0
dap_wolf = 0

for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            sheep = 0
            wolf = 0
            bfs(i, j)
            if sheep > wolf:
                dap_sheep += sheep
            else:
                dap_wolf += wolf

print(dap_sheep, dap_wolf)