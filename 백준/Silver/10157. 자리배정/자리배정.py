di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]

i, j, cnt,dr = R-1, 0, 1,0  # 초기화
arr[i][j] = cnt     # 넣어줘야 됌 필수
cnt += 1

while cnt <= C*R:
    ni, nj = i+di[dr], j+dj[dr]
    if 0<=ni<R and 0<=nj<C and arr[ni][nj] == 0:
        i, j = ni, nj
        arr[i][j] = cnt
        cnt += 1
    else:
        dr = (dr+1) % 4

dap_i, dap_j = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == K:
            dap_i = j + 1
            dap_j = R - i


if dap_i and dap_j:
    print(dap_i, dap_j)
else:
    print(0)