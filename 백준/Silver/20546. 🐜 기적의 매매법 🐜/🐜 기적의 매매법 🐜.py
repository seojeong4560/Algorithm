money = int(input())
stocks = list(map(int, input().split()))

# bnp 주식 개수
bnp = 0
# timing 주식 개수
timing = 0

# bnp
bnp_money = money
bnp_dap = 0
for stock in stocks:
    if stock <= bnp_money:
        bnp += (bnp_money//stock)
        bnp_money -= (bnp_money//stock)*stock

bnp_dap = (stocks[13]*bnp) + bnp_money

# timing

# 연속으로 내려간 날
down_count = 0
# 연속으로 올라간 날
up_count = 0
# 현재 stock과 비교할 그 전날 stock
before_stock = 0
# 현재 stock
now_stock = 0

timing_money = money
timing_dap = 0
for i in range(1, len(stocks)):
    before_stock = stocks[i-1]
    now_stock = stocks[i]
    # 매수
    if before_stock > now_stock:
        down_count += 1
        up_count = 0
        if down_count >= 3:
            timing += (timing_money // stocks[i])
            timing_money -= (timing_money//stocks[i])*stocks[i]

    # 매도
    if before_stock < now_stock:
        up_count += 1
        down_count = 0
        if up_count >= 3:
            timing_money += timing * stocks[i]
            timing = 0

    # 초기화
    if before_stock == now_stock:
        down_count = 0
        up_count = 0

timing_dap = (stocks[13] * timing) + timing_money

if bnp_dap > timing_dap:
    print('BNP')
elif bnp_dap < timing_dap:
    print('TIMING')
else:
    print('SAMESAME')
