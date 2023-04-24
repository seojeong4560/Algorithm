N, M ,R = map(int, input().split())

arr = [list(map(int, input().split()))for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M)//2):
        # x, y는 돌려지는 배열 중 가장 첫 번째 배열 인덱스
        x, y = i, i
        tmp = arr[x][y]

        # 안쪽까지 계속 고려해야 하기 때문에 n-i랑 m-i까지로 범위 설정

        # 좌
        for j in range(i+1, N-i):
            x = j
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

        # 하
        for j in range(i+1, M-i):
            y = j
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

        # 우 
        for j in range(i+1, N-i):
            x = N - j - 1
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

        # 상
        for j in range(i+1, M-i):
            y = M - j - 1
            prev_value = arr[x][y]
            arr[x][y] = tmp
            tmp = prev_value

for i in range(N):
    for j in range(M):
        print(arr[i][j], end =" ")
    print()
