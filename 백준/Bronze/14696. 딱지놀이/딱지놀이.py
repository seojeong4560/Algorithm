def change(A, B):
    for i in range(4, 0, -1):
        if A[1:].count(i) > B[1:].count(i):
            return 'A'
        elif A[1:].count(i) < B[1:].count(i):
            return 'B'
    else:
        return 'D'

N =int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(change(A[1:], B[1:]))