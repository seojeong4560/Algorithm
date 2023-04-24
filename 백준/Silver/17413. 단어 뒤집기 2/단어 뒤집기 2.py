# list로 만들어주는거 주의
word = list(input())

i = 0
start = 0

while i < len(word):
    # 열린 괄호를 만나면
    if word[i] == "<":
        i += 1
        # 닫힌 괄호를 만날 때 까지
        while word[i] != ">":
            i += 1
        # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킴
        i += 1
    # 숫자나 알파벳을 만나면
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        # 숫자, 알파벳 범위에 있는 것들을
        tmp = word[start:i]
        # 뒤집기
        tmp.reverse()
        word[start:i] = tmp
    # 괄호도 아니고 알파 숫자도 아니면
    # 즉 공백이면
    # 그냥 증가시키기
    else:
        i += 1

print("".join(word))