def fib(N):
    # 0이 출력되는 횟수 리스트
    zeros = [1, 0, 1]
    # 1이 출력되는 횟수 리스트
    ones = [0, 1, 1]
    
    # append해서 추가하는 거 핵심
    if N >= 3:
        for i in range(2, N):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    
    print(zeros[N], ones[N])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    fib(N)