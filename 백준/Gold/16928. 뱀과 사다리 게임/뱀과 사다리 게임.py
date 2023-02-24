from collections import deque

def bfs(v):
    deq = deque()
    deq.append(v)
    visited[v] = 1

    while deq:
        target = deq.popleft()

        # 주사기 굴리기
        for i in range(1, 7):
            dice = target + i

            if dice > 100:
                continue

            cnt = arr[dice]

            if not visited[cnt]:
                deq.append(cnt)
                visited[cnt] += visited[target] + 1

                if cnt == 100:
                    return
                
            

        
# N 사다리 수 M 뱀의 수
N, M = map(int, input().split())

arr = [i for i in range(101)]

for _ in range(N + M):
    a, b = map(int, input().split())
    arr[a] = b

visited = [0] * 101

bfs(1)

print(visited[100]-1)