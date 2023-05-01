N = int(input())    # 색종이 종이 장수
N_list = [list(map(int, input().split()))for _ in range(N)]
n = 0
for i in range(N):
    for j in range(4):
        if N_list[i][j] > n:
            n = N_list[i][j]

# 격자판 만들기
M_arr = [[0]* (n+300) for _ in range(n+300)]

# 첫번째 들어온거 +1 두번째 들어온거 +1 .. 씩해서 부분 면적 구하기

for i in range(N):
    for a in range(N_list[i][0], N_list[i][0] + N_list[i][2]):
        for b in range(N_list[i][1], N_list[i][1] + N_list[i][3]):     # 예제로 하면 (4, 2) 해서 범위 오류
            M_arr[a][b] = i + 1

for i in range(1, N+1):
    dap = 0
    for a in range(n+300):
        for b in range(n+300):
            if M_arr[a][b] == i:
                dap += 1
    print(dap)