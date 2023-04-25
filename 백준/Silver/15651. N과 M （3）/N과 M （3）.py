def dfs():
    if len(s) == M:
        for i in range(M):
            print(s[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        s.append(i)
        dfs() 
        s.pop()

N, M = map(int, input().split())

s = []

dfs()