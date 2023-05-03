from itertools import permutations
# N 민혁이가 영수에게 질문 한 수
N = int(input())

# 1 ~ 9 까지 모든 수 중에서 3개를 뽑아서 조합한 리스트 만들어 놓기(핵심)
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(N):
    # n 민혁이가 질문한 세자리수 s 스트라이크 개수 b 볼 개수
    n, s, b = map(int, input().split())
    # 질문한 세 자리수 string으로 만들기 
    n = list(str(n))
    remove_cnt = 0

    for i in range(len(num)):
        strike = ball = 0
        # num[0] 부터 시작
        # 계속해서 조합 리스트의 처음 원소부터 각각 비교해주기 위해
        # i 인덱스를 0부터 시작하도록 만들어 주는 것
        # 삭제한 자리에서 시작하기 위해??
        i -= remove_cnt 
        for j in range(3):
            # 조건이 strike 이면
            if num[i][j] == n[j]:
                strike += 1
            # 조건이 ball 이면
            elif n[j] in num[i]:
                ball += 1

        # 최종적으로 영수가 대답해준 s와 b의 개수와 맞는지 비교해서
        # 개수가 맞지 않으면 1에서 만든 조합 리스트에서 해당 수 제거
        if (strike != s) or (ball != b):
            num.remove(num[i])
            remove_cnt += 1

# 남아있는 num의 개수(길이)가 정답
print(len(num))