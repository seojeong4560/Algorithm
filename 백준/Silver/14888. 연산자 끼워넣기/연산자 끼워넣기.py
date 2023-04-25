def dfs(depth, result, plus, minus, mul, div):
    # global 안해주면 오류
    global dap_min, dap_max

    # max min 조심 계속 max해서 틀렸음
    if depth == N:
        dap_max = max(dap_max, result)
        dap_min = min(dap_min, result)
        # 이왕이면 return 해주기
        return

    # + - * // 등호 조심
    if plus:
        dfs(depth+1, result + num[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, result - num[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, result * num[depth], plus, minus, mul-1, div)
        # result 부분 조심 틀림
    if div:
        dfs(depth+1, int(result / num[depth]), plus, minus, mul, div-1)




# 숫자 개수
N = int(input())

# 숫자
num = list(map(int, input().split()))

# 연산자 덧셈 뺄셈 곱셈 나눗셈
op = list(map(int, input().split()))

# 충분하게 두지 않아서 틀렸음
dap_min = 100000000000
dap_max = -100000000000

dfs(1, num[0], op[0], op[1], op[2], op[3])

print(dap_max)
print(dap_min)