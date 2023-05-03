# 다시 풀어보기
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    global dap

    if 0 <= x < n and 0 <= y < m and arr[x][y]:
        arr[x][y] = 0
        dap += 1

        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x-1, y)

    else:
        return


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dap_max = 0
dap_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            dap_cnt += 1
            dap = 0
            dfs(i, j)
            if dap > dap_max:
                dap_max = dap

print(dap_cnt)
print(dap_max)