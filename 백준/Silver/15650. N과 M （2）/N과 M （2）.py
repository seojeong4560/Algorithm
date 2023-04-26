def dfs(start):
    if len(c) == M:
        for i in range(M):
            print(c[i], end=' ')
        print()
        return

    # 기존에는 1부터 n까지 모든 숫자를 사용했지만 
    # [2, 1]과 같이 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외하기 위해
    # start부터 n까지의 숫자를 사용
    # 재귀함수를 호출할 때는 i를 이용하여 자신의 다음 숫자를 부르게 됌
    for i in range(start, N+1):
        if i not in c:
            c.append(i)
            dfs(i+1)
            c.pop()


N, M = map(int, input().split())
c = []

dfs(1)