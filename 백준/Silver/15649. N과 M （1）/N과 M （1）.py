def dfs():
    # 리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나옴
    if len(s) == M:
        print(' '.join(map(str, s)))

    for i in range(1, N+1):
        # 중복이 아니면 숫자 i를 리스트 s에 넣기
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
            # 위 코드 설명
            # : 현재 s = [1]인 상태에서 다음 숫자를 넣기 위하여 가지치기하기(재귀함수)
            # : 만약 n = 4, m = 2라면 
            # : s: [1] -> [1, 2] -> [1] -> [1, 3] -> [1] -> [1, 4]
            # :            출력    pop(2)    출력    pop(3)    출력


N, M = map(int, input().split())

# 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트
s = []

dfs()
