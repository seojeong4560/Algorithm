N, M = map(int, input().split())
num = int(input())

garo = [0, M]
sero = [0, N]

for i in range(num):
    garo_sero, length = map(int, input().split())
    if garo_sero == 0:
        garo.append(length)
    else:
        sero.append(length)

garo.sort()
sero.sort()

garo_max = []
garo_max.append(garo[0])
garo_max.append(M - garo[-1])
for i in range(1, len(garo)):
    garo_max.append(garo[i]-garo[i-1])

sero_max = []
sero_max.append(N - sero[-1])
sero_max.append(sero[0])
for i in range(1, len(sero)):
    sero_max.append(sero[i]-sero[i-1])

print(max(garo_max) * max(sero_max))