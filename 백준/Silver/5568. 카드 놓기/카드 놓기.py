def dfs():
    global dap 

    if len(s) == k:
        dap.add(''.join(map(str, s)))
        return

    for i in range(len(num)):
        if not check[i]:
            s.append(num[i])
            check[i] = 1
            dfs()
            s.pop()
            check[i] = 0


        # if num[i] not in s:
        #     s.append(num[i])
        #     dfs()
        #     s.pop()


# n장의 카드 
n = int(input())
# k개 선택
k = int(input())

num = []
for i in range(n):
    tmp = int(input())
    num.append(tmp)

s, dap =[], set()
check = [0] * n

dfs()

print(len(dap))