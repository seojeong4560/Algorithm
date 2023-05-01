N, K = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

# 금메달이 많은 순으로 정렬을 하고
# 금메달이 같다면 은메달
# 은메달이 같다면 동메달 순으로 정렬
# 핵심
arr.sort(key=lambda x : (-x[1], -x[2], -x[3]))

# 국가 번호의 index를 찾기
# 핵심
for i in range(N):
    if arr[i][0] == K:
        index = i

# 정렬된 배열을 검사하며 
# 국가 번호 index의!!! 금메달 은메달 동메달의 수와 같다면
# index가 다르더라도 구하고자 하는 국가 번호의 index에 있는 금은동이 같으면 출력
# 위 과정을 통해 동 순위 처리를 진행 할 수 있음
# 핵심
for i in range(N):
    if arr[index][1:] == arr[i][1:]:
        print(i+1)
        break