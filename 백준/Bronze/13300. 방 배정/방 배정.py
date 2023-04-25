N, K = map(int, input().split())            # N: 학생수 K: 최대 인원 수

girl = [0] * 7
boy = [0] * 7

dap1 = 0
dap2 = 0

for _ in range(N):
    S, Y = map(int, input().split())        # S: 성별 Y: 학년

    if S == 0:  # 여자 이면
        girl[Y] += 1
    else:
        boy[Y] += 1


for i in range(len(girl)):
    if girl[i] > 0:
        if girl[i] - K <= 0:
            dap1 += 1
            girl[i] = 0
        elif girl[i] - K > 0:
            while girl[i] > 0:
                dap1 += 1
                girl[i] = girl[i] - K


for i in range(len(girl)):
    if boy[i] > 0:
        if boy[i] - K <= 0:
            dap2 += 1
            boy[i] = 0
        elif boy[i] - K > 0:
            while boy[i] > 0:
                dap2 += 1
                boy[i] = boy[i] - K

print(dap1+dap2)