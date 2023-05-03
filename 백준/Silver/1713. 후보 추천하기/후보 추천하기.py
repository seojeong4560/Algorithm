# 사진 틀의 개수
N = int(input())

# 총 추천 횟수
vote = int(input())

# 추천 학생 번호
students = list(map(int, input().split()))

# 사진틀
picture = []
# 사진틀 인덱스와 매치해서 추천 수 저장할 리스트
score = []

for i in range(vote):
    # 사진틀에 있으면
    if students[i] in picture:
        for j in range(len(picture)):
            if students[i] == picture[j]:
                score[j] += 1

    # 사진틀에 없으면
    else:
        # 사진틀 꽉차있으면
        if len(picture) >= N:
            for j in range(N):
                # 가장 작은 점수 찾고
                if score[j] == min(score):
                    del picture[j]
                    del score[j]
                    break
        # 새로운거 뒤에 더해줌
        picture.append(students[i])
        score.append(1)

picture.sort()
for i in range(len(picture)):
    print(picture[i], end= " ")