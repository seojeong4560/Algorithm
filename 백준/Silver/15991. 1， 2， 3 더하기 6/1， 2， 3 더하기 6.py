dp = [0, 1, 2, 2, 3, 3, 6] + [0] * (100001 - 7)

for i in range(7, 100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(dp[N])