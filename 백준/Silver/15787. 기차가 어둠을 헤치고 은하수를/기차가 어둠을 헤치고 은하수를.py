# N 기차의 수 M 명령어의 수
N, M = map(int, input().split())

# 명령
arr = [list(map(int, input().split())) for _ in range(M)]

# 기차
train = [[0]*20 for _ in range(N)]

for i in range(M):
    # 기차 순서에서 -1해줘야 함 주의주의 
    # 다른데도 -1 해야됨 주의주의
    # 명령어 1
    if arr[i][0] == 1:
        # 사람이 없다면 사람 태우기
        if train[arr[i][1]-1][arr[i][2]-1] == 0:
            train[arr[i][1]-1][arr[i][2]-1] = 1


    # 명령어 2
    elif arr[i][0] == 2:
        # 사람이 있다면 사람 하차시키기
        if train[arr[i][1]-1][arr[i][2]-1] == 1:
            train[arr[i][1]-1][arr[i][2]-1] = 0

        

    # 명령어 3
    elif arr[i][0] == 3:
        # 기차에 있는 승객 모두 한칸씩 뒤로 

        for a in range(19, 0, -1):
            train[arr[i][1]-1][a] = train[arr[i][1]-1][a-1]
        # 가장 앞에 있던 승객은 마지막에 그 자리를 비워주어야 함 
        train[arr[i][1]-1][0] = 0

    # 명령어 4
    elif arr[i][0] == 4:
        # 기차에 있는 승객 모두 한칸씩 앞으로
        for a in range(19):
            train[arr[i][1]-1][a] = train[arr[i][1]-1][a+1]
        train[arr[i][1]-1][19] = 0

state = []

cnt = 0
for i in range(N):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1

print(cnt)
