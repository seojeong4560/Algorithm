# 모눈종이의 크기 h w
h, w = map(int, input().split())
# 스티커의 수 n
n = int(input())
# 스티커의 크기 R C
stk = list(list(map(int, input().split())) for _ in range(n))

dap = 0
for i in range(n):
    for j in range(i+1, n):
        # 스티커 두개를 고르는 거니까
        r1, c1 = stk[i]
        r2, c2 = stk[j]

        # 스티커 중 두개를 골라 다음 조건에 맞는지 검사
        # 여기서 경우의 수는
        # 둘 다 회전하지 않는 경우
        # 첫 번째 스티커만 회전한 경우
        # 두 번재 스티커만 회전한 경우
        # 둘 다 회전한 경우
        if(r1+r2<=h and max(c1, c2)<=w) or (max(r1, r2) <= h and c1+c2<=w):
            dap = max(dap, r1*c1 + r2*c2)
        if(c1+r2<=h and max(r1, c2)<=w) or (max(c1, r2)<=h and r1+c2<=w):
            dap = max(dap, r1*c1 + r2*c2)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            dap = max(dap, r1*c1 + r2*c2)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            dap = max(dap, r1*c1 + r2*c2)

print(dap)
