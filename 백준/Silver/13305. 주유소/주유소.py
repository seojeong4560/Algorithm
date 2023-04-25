
# 도시의 개수
N = int(input())

# 인접한 두 도시를 연결하는 도로의 길이
km_list = list(map(int, input().split()))

# 주유소의 리터당 가격
money_list = list(map(int, input().split()))

# 시작점에서는 반드시 주유가 되어있어야함
# 첫 최소 비용은 시작점의 가격
min_money = money_list[0]

# 구하고자 하는 답
# 일단 처음 시작때 필요한 값으로
dap = min_money * km_list[0]

for i in range(1, N-1):
    # 더 저렴한 도시를 발견하게 되면
    if money_list[i] < min_money:
        min_money = money_list[i]
    dap += min_money * km_list[i]

print(dap)