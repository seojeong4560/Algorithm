import re
p = re.compile('[A-F]?A+F+C+[A-F]?')
N = int(input())
for _ in range(N):
    k = input()
    if p.fullmatch(k):
        print('Infected!')
    else:
        print('Good')