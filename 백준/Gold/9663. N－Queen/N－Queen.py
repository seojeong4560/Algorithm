def check(x):
    for i in range(x):
        # 열이 같거나 대각선이 같으면 false
        if row[x] == row[i] or abs(row[x]-row[i]) == x - i:
            return False
    return True


def dfs(x):
    global dap

    if x == N:
        dap += 1

    else:
        # 각 행에 퀸 놓기
        # i는 열 번호 0부터 N 전까지 옮기면서 유망한 곳 찾기
        for i in range(N):
            row[x] = i
            # 행 열 대각선 체크 함수 True이면 백트래킹 안하고 계속 진행
            if check(x):
                dfs(x + 1)


N = int(input())
row = [0] * N
dap = 0

dfs(0)
print(dap)
