# 듣도 보도 못한 사람의 수 입력 받기
N, M = map(int, input().split())

# a, b 변수로 각각 중복이 없는 set의 특성을 활용해서 
# 입력 받은 문자들을 add() 해주기
a = set()
for _ in range(N):
    a.add(input())

b = set()
for _ in range(M):
    b.add(input())

# dap 변수를 추가해서
# set a, b에 교집합 &를 해서 중복되는 문자열을 선택하고
# list()로 묶어서 리스트화 시키기
# 명단을 사전순으로 제출해야 하니 sorted()로 a,b,c,d 순서로 바꿔주면 제출 준비 끝
dap = sorted(list(a&b))

print(len(dap))

for i in dap:
    print(i)