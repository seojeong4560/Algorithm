#앞의 숫자와 비교해야하므로 파라미터로 넘겨줌
def dfs(start):
    if len(s) == M:
        for i in range(M):
            print(s[i], end=' ')
        print()
        return

    # 기존에는 1부터 n까지 모든 숫자를 사용했지만 
    # [2, 1]과 같이 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외하기 위해
    # start부터 n까지의 숫자를 사용
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()


N, M = map(int, input().split())
s = []

dfs(1)