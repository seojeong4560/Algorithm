from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    deq = deque()
    deq.append((i, j))
    visited[i][j] = 1

    # 연합된 국가 담기
    union = [(i, j)]
    # 총 연합된 인원 수
    count = arr[i][j]

    # 인접 국가를 탐색하면서 인구차이 l명 이상 r명 이하인 경우 연합 국가에 담기
    while deq:
        x, y = deq.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                union.append((nx, ny))
                visited[nx][ny] = 1
                deq.append((nx, ny))
                count += arr[nx][ny]

    # 연함 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산
    for x, y in union:
        arr[x][y] = count // len(union)

    return len(union)

# 변수 순서 주의하자... 이거 때문에 10분 날림
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 인구 이동 횟수, 구하고자 하는 답
dap = 0
# 인구 이동 존재 유무 체크
flag = 0

# 인구 이동이 없을 때까지 반복
while True:
    visited = [[0] * n for _ in range(n)]
    # 인구 이동 존재 유무 체크
    flag = 0
    # 모든 곳을 bfs로 방문하여 연합 진행
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = 1
    # 인구 이동이 한 번도 없는 경우 그만하기
    if flag == 0:
        break
    dap += 1


print(dap)