from collections import deque
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(sx, sy):

    deq = deque()
    deq.append((sx, sy))

    while deq:
        nowx, nowy = deq.popleft()
        # 이동하려는 칸에 도달하면 return
        if nowx == endx and nowy == endy:
            return board[nowy][nowx]

        for a in range(8):
            nx = nowx + dx[a]
            ny = nowy + dy[a]
            # 범위에 있고 방문 안했으면
            if 0 <= nx < l and 0 <= ny < l and board[ny][nx] == 0:
                board[ny][nx] = board[nowy][nowx] + 1
                deq.append((nx, ny))
                

# 테스트 케이스 개수
T = int(input())
for _ in range(T):

    # 테스트 케이스 한 변의 길이
    l = int(input())
    board = [[0]*l for _ in range(l)]

    # 현재 나이트가 있는 칸
    startx, starty = map(int, input().split())
    # 나이트가 이동하려고 하는 칸
    endx, endy = map(int, input().split())

    # 최소 몇 번 만에 이동할 수 있는지 => bfs돌리기
    dap = bfs(startx, starty)

    print(dap)