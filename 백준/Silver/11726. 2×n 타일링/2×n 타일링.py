n = int(input())

s = [0] * 1002
s[1] = 1
s[2] = 2

for i in range(3, 1001):
    s[i] = s[i-2] + s[i-1]

print(s[n] % 10007)
