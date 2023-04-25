# 알고리즘: 리스트에서 가장 큰 수를 리스트 중간에 넣고 그 다음 큰 수부터 차례대로 왼쪽 오른쪽 배치

T = int(input())

for tc in range(1, T+1):
    
    # 통나무의 개수
    N = int(input())

    # 통나무의 높이를 나타내는 정수
    L_list = list(map(int, input().split()))

    L_list.sort()
    dap_list = [L_list[-1]]
    L_list.pop(-1)

   
    while len(L_list) > 0:

        dap_list.insert(0, L_list[-1])
        L_list.pop(-1)

        if len(L_list) == 0:
            break
        else:
            dap_list.append(L_list[-1])
            L_list.pop(-1)

    dap = 0
    for i in range(N-1):
        if dap < abs(dap_list[i]-dap_list[i+1]):
            dap = abs(dap_list[i]-dap_list[i+1])

    print(dap)