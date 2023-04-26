# 오리 울음소리 문자열
duck = input()
# 방문한 문자는 visited 리스트를 만들어 방문처리 하기 
visited = [0] * len(duck)
cnt = 0

# 녹음한 소리가 올바르지 않은 경우
# 문자열의 길이가 5의 배수가 아닐 때
if len(duck) % 5 != 0:
    print(-1)
    exit()

# quack 문자를 만들어서 q를 방문했으면 
# index를 증가시켜서 다음 u와 비교하기 
def solve(start):
    global cnt
    quack = 'quack'
    index = 0
    flag = 1
    for i in range(start, len(duck)):
        if duck[i] == quack[index] and not visited[i]:
            visited[i] = 1
            if duck[i] == 'k':
                if flag:
                    cnt += 1
                    flag = 0
                index = 0
                continue
            index += 1

for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        solve(i)

# 녹음한 소리가 올바르지 않은 경우
# 문자열을 모두 방문하지 않을 때
# 오리가 0마리 일 때
if not all(visited) or cnt == 0:
    print(-1)
else:
    print(cnt)