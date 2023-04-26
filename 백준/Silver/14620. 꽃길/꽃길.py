# 본래 자리를 포함한 4방향에 이미 꽃을 심었다면
# False를 아니면 True를 리턴
def check(a, b):
    for i in range(5):
        x = a + di[i]
        y = b + dj[i]
        if visited[x][y] == 1:
            return False
    return True

def dfs(flower):
    global total, dap
    
    # 꽃을 3개 다 심었을 때 최소 코스트 갱신
    if flower == 3:
        dap = min(dap, total)
        return
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            # 5 공간에 이미 심지 않았다면
            if check(i, j):
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 1
                    total += arr[x][y]

                dfs(flower+1)

                # 다음 재귀를 위해 초기화
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 0
                    total -= arr[x][y]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]
dap = 9999999999999
total = 0
dfs(0)
print(dap)