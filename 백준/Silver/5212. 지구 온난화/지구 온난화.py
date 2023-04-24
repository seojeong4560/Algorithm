import copy
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# R 세로 C 가로
R, C = map(int, input().split())

# 입력 지도
arr = [list(input()) for _ in range(R)]
new_arr = copy.deepcopy(arr)
land_cnt = 0

for x in range(R):
    for y in range(C):
        if arr[x][y] == 'X':
            cnt = 0
            land_cnt += 1
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                # 모서리에 섬이 있는 경우
                # 인접한 칸은 범위 밖으로 넘어가며 바다라고 취급하여 카운트한다.
                if 0 > nx or nx >= R or 0 > ny or ny >= C:
                    cnt += 1
                # 모서리가 아닌 부분에 섬이 있을 때
                elif 0 <= nx < R and 0 <= ny <C:
                    if arr[nx][ny] == '.':
                        cnt += 1
            if cnt >=3:
                new_arr[x][y] = '.'
                land_cnt -= 1

# 섬은 적어도 하나가 있다
if land_cnt == 0:
    print('X')
else:
    startR = 0
    endR = 0

    for i in range(R):
        if 'X' in new_arr[i]:
            startR = i
            break
        
    for i in range(R-1, -1, -1):
        if 'X' in new_arr[i]:
            endR = i
            break

    idx = []
    for j in range(C):
        for i in range(startR, endR + 1):
            if 'X' == new_arr[i][j]:
                idx.append(j)
                break

    for i in new_arr[startR:endR+1]:
        print(''.join(i[idx[0]:idx[-1]+1]))