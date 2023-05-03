# dx dy 각 쌍 순서 맞춰야함 주의 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
f_number = int(input())

arr = [[0] * N for _ in range(N)]

i = -1
j = 0
k = N*N
d = 0

while k > 0:
    ni = i + dx[d]
    nj = j + dy[d]

    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
        i = ni
        j = nj
        arr[i][j] = k 

        k -= 1

    else:
        d = (d + 1) % 4

# 표 출력
for i in range(N):
    print(" ".join(map(str, arr[i])))

# 좌표 출력
for i in range(N):
    for j in range(N):
        if arr[i][j] == f_number:
            print(i+1, j+1)