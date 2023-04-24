from itertools import product

# n보다 작은 수 k개의 원소
n, k = map(int, input().split())
# n의 길이
len_max = len(str(n))
k_list = list(input().split())

while True:
    # repeat를 통해 몇 개를 뽑을지 결정
    # product는 중복 순열(순열은 순열인데 '중복')을 구하는 것
    # repeat 활용하는 거 잘 알아두자!
    tmp = list(product(k_list, repeat=len_max))
    dap = []

    for i in tmp:
        # int로 바꿔서 비교해야 되는 거 주의
        if int("".join(i)) <= n:
            dap.append(int("".join(i)))

    if len(dap) >= 1:
        print(max(dap))
        break

    # 점점 중복 순열의 길이를 줄이면서
    # 처음 길이 일 때가 당연히 가장 큰 값일 가능성이 있기 때문임
    else:
        len_max -= 1