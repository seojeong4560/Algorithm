def dfs(start):
    # global dap 해주는거 까먹지 말기
    # 안하면 오류 남
    # dap은 변하니까
    global dap
    
    # num_list에는 음수도 있기 때문에 len도 고려해야함 
    if sum(c) == S and len(c) > 0:
        dap += 1
        

    for i in range(start, N):
        # num_list 안에는 같은 숫자가 있을 수 있기 때문에 
        # if num_list[i] not in c: 이 조건은 있으면 안된다.
        c.append(num_list[i])
        dfs(i+1)
        c.pop()


N, S = map(int, input().split())
num_list = list(map(int, input().split()))

c = []
dap = 0

dfs(0)

print(dap)