N, M = map(int, input().split())
dap = 100000000000
w_row = 'WBWBWBWB'
b_row = 'BWBWBWBW'

arr = [list(input()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            row = arr[k][j:j+8]
            for v in range(8):
                if k % 2 ==0:
                    if w_row[v] != row[v]:
                        w += 1
                    if b_row[v] != row[v]:
                        b += 1
                else:
                    if b_row[v] != row[v]:
                        w += 1
                    if w_row[v] != row[v]:
                        b += 1
        dap = min(dap, w, b)

print(dap)