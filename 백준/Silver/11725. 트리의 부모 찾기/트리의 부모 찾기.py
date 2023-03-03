import sys
sys.setrecursionlimit(10**8)

def dfs(tree, s, parents):
    # 연결된 노드들부터 parents[i]의 부모가 없으면 부모 설정 해주고, DFS 돌리기
    for i in tree[s]:
        # 만약 방문하지 않은 노드라면
        if parents[i] == 0:
            # 부모 노드로 저장
            parents[i] = s
            dfs(tree, i, parents)

# 노드 개수
N = int(input())

# 트리
tree = [[] for _ in range(N+1)]

# 부모
parent = [0 for _ in range(N+1)]

# 트리 구조 입력
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(tree, 1, parent)

for i in range(2, N+1):
    print(parent[i])