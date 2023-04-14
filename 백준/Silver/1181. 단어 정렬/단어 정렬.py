N = int(input())

lst = []

for _ in range(N):
    lst.append(input())

# set으로 변환해서 중복값 제거
set_lst = set(lst)

# 다시 list로 변환
lst = list(set_lst)

# sort 정렬이 문자까지 정렬해줌
# 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해준다
lst.sort()
# 문자열 길이 순으로 정렬
lst.sort(key=len)

for i in lst:
    print(i)