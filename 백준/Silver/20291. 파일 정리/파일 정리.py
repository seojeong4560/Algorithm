# 파일 개수 N
N = int(input())

arr = []
# 딕셔너리 생각하내는 것이 핵심
dict = {}

for _ in range(N):
    # 핵심
    # N개의 파일 이름과 확장자를 '점(.)'을 기준으로 나눠서 입력받기
    file = input().split('.')
    # 파일의 확장자만 arr에 추가하기 
    arr.append(file[1])

# arr안에서 미리 선언해둔 딕셔너리 dict를 이용해 리스트 속 각 확장자의 개수를 구하기
for i in arr:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1

# 딕셔너리를 items() 함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있음
# 키 값(확장자 이름)을 기준으로 정렬
dict = sorted(dict.items())

# 출력 형식에 맞춰서 확장자 이름과 그 개수를 출력하기 
for i, j in dict:
    print(i, j)