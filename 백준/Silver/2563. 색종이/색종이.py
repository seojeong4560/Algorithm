N = int(input())        # 색종이 장수
dap_arr = [[0] * 101 for _ in range(101)]
dap = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            dap_arr[i][j] += 1

for i in range(101):
    for j in range(101):
        if dap_arr[i][j] > 0:
            dap += 1

print(dap)
