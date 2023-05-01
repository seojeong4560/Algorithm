import sys
import itertools
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

# 순열
permu = itertools.permutations(data, N)

dap = 0

for p in list(permu):
    sumP = 0

    for i in range(N-1):
        sumP += abs(p[i]-p[i+1])

    if sumP > dap:
        dap = sumP

print(dap)
