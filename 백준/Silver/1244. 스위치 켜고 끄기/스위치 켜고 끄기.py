def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

# 스위치의 개수
N = int(input())

# 스위치 
# 스위치 번호가 1번부터 시작해서 앞에 [-1] 추가
switch = [-1] + list(map(int, input().split()))

students = int(input())

for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)

    # 여자
    else:
        change(num)
        for a in range(N//2):
            if num + a > N or num - a < 1: break
            if switch[num+a] == switch[num-a]:
                change(num+a)
                change(num-a)
            else:
                break
            
for i in range(1, N+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
