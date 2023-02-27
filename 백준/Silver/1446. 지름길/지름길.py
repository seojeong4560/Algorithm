n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최단거리 테이블 생성
dp = [i for i in range(d+1)]

# 0 부터 고속도로의 길이까지 반복하여 확인
for i in range(d+1):
    # 지름길 거리와 고속도로로 간 거리 비교
    dp[i] = min(dp[i], dp[i-1]+1)

    # 지름길을 반복하여 최단 거리 찾기
    for s, e, l in arr:
        if i == s and e <= d and dp[i]+l < dp[e]:
            dp[e] = dp[i]+l
print(dp[d])