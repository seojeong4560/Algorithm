from collections import deque

def bfs(x):
    deq = deque()
    deq.append(x)

    visited[x] = 1

    while deq:
        x = deq.popleft()

        if x == K:
            print(visited[x]-1)
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                # 순간이동 하는 경우는 0초 걸림
                if nx == x*2:
                    visited[nx] = visited[x] 
                    deq.appendleft(nx)

                # 걷는 경우는 1초 걸림
                else:
                    visited[nx] = visited[x] + 1
                    deq.append(nx)

                
# N 수빈이 위치 K 동생 위치
N, K = map(int, input().split())

visited = [0] * 100001

bfs(N)