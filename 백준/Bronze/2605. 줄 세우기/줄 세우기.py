N = int(input())
num_list = list(map(int, input().split()))

dap = [1]
student = 2
idx = 0

for i in range(1, N):
    if num_list[i] == 0:
        dap.append(student)
        idx += 1
    else:
        dap.insert(idx-num_list[i]+1, student)
        idx += 1

    student += 1

for i in range(len(dap)):
    if dap[i] > 0:
        print(dap[i], end = ' ')