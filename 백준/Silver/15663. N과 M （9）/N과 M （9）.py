def dfs(depth):
    if depth == M:
        for i in range(M):
            print(s[i], end = ' ')
        print()
        return

    # overlap 이란 변수를 만들어서 전에 쓰인 변수 값과 비교하는 것
    # 위치는 탈출문 바로 아래쪽에 위치하기(깊이가 다를 때마다 변수를 초기화 해야함)
    # overlap으로 중복된 수열을 출력하는 것을 방지
    # 예를들어 overlap 없으면 첫 번째 테스트 케이스에서 2 4 4 로 나와버림
    # visited로 방문해야 될 숫자 구별
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != L[i]:
            visited[i] = 1
            s.append(L[i])
            overlap = L[i]
            dfs(depth +1)
            visited[i] = 0
            s.pop()

N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [0] * N
s = []

dfs(0)
