from collections import deque

dx = [-2, -2, 0, 0, +2, +2]
dy = [-1, +1, -2, +2, -1, +1]

def bfs():
    global r1, c1

    deq = deque()
    deq.append((r1, c1))
    visited[r1][c1] = 1

    while deq:
        r1, c1 = deq.popleft()

        # 여기서 if문 써서 print하려고 했으나
        # 문제에서 이동할 수 없는 경우도 있으므로 안 됨

        # 무작정 4로 쓰지 말기... 습관 조심
        for a in range(6):
            nr1 = r1 + dx[a]
            nc1 = c1 + dy[a]
            if 0 <= nr1 < N and 0 <= nc1 < N and not visited[nr1][nc1]:
                # (+ 1)도 당연히 계속 추가적으로 더해주어야 함 
                # 아니면 이동 횟수가 더해지지 않고 그냥 같은 값 나와버림
                visited[nr1][nc1] += visited[r1][c1] + 1
                deq.append((nr1, nc1))
                
N = int(input())

r1, c1, r2, c2 = map(int, input().split())
# 방문 체크 뿐 만 아니라 이동 횟수를 체크하기 위한 리스트
visited = [[0] * N for _ in range(N)]

bfs()

# r2 c2가 아닌 r1 c1으로 잘못 쳐서 헤맸음
# 출력은 당연히 -1을 빼서 출력해 줘야함 시작부터 1을 더했기 때문
print(visited[r2][c2]-1)