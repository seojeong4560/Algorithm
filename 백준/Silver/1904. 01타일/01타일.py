N = int(input())

dp = [0] * 10000001
dp[1] = 1
dp[2] = 2

for a in range(3, N+1):
    dp[a] = (dp[a-1] + dp[a-2]) % 15746

print(dp[N])