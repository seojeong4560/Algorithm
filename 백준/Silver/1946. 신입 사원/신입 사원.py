import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    score_list = [list(map(int, input().split())) for _ in range(N)]

    score_list.sort()
    min_rank = score_list[0][1]

    cnt = 1

    for i in range(N):
        if score_list[i][1] < min_rank:
            cnt += 1
            min_rank = score_list[i][1]

    print(cnt)