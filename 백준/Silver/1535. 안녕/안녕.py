from itertools import combinations

N = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))

# 처음부터 전체 소모 health합이 100보다 작으면 happy출력
if sum(health) < 100:
    print(sum(happy))
    
else:
    c = []
    
    # c 리스트에 health와 happy 값 같이 넣기
    for i in range(N):
        c.append([health[i], happy[i]])

    max_happy = 0
    for i in range(N):
        # 추출개수가 1부터 N개인 조합 만들기
        comb = list(combinations(c, i+1))

        for j in comb:
            hp = 0
            ha = 0
            for k in range(len(j)):
                hp += j[k][0]
                ha += j[k][1]
            # 조건을 만족하면 
            if hp < 100 and ha > max_happy:
                max_happy = ha
    print(max_happy)
