N = int(input())        # 스위치의 개수
N_list = [2] + list(map(int, input().split()))      # 앞에 [2]를 추가해 준 것은 나중에 여학생의 경우 대칭을 검증하기 위해서임
M = int(input())        # 학생수
M_arr = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    if M_arr[i][0] == 1:        # 남이면 배수 상태로 바꿔주기
        for a in range(1, N+1):
            if a % M_arr[i][1] == 0:                # 배수이면
                if N_list[a] == 1:
                    N_list[a] = 0
                else:
                    N_list[a] = 1

    elif M_arr[i][0] == 2:      # 여이면 대칭으로 상태 바꾸기
        m = M_arr[i][1]
        if N_list[m] == 1:
            N_list[m] = 0
            for a in range(1, N - m + 1):
                if N_list[m - a] == N_list[m + a] == 1:
                    N_list[m - a] = N_list[m + a] = 0

                elif N_list[m - a] == N_list[m + a] == 0:
                    N_list[m - a] = N_list[m + a] = 1

                else:
                    break

        elif N_list[m] == 0:
            N_list[m] = 1
            for a in range(1, N - m + 1):
                if N_list[m - a] == N_list[m + a] == 1:
                    N_list[m - a] = N_list[m + a] = 0

                elif N_list[m - a] == N_list[m + a] == 0:
                    N_list[m - a] = N_list[m + a] = 1

                else:
                    break

# 출력: 한줄에 20개씩 출력
count = 0
for i in range(1, N+1):
    print(N_list[i], end = ' ')
    count += 1

    if count == 20:
        print()
        count = 0