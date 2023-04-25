N = int(input())
stars = [[' ' for _ in range(4*N-3)] for _ in range(4*N-3)]

def fill_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return
    
    length = 4 * n - 3

    for i in range(length):
        # 1번 선분
        stars[y][x+i] = '*'
        # 2번 선분
        stars[y+i][x] = '*'
        # 3번 선분
        stars[y+length-1][x+i] = '*'
        # 4번 선분
        stars[y+i][x+length-1] = '*'

    # N이 하나씩 줄 때마다 x, y 좌표가 2씩 증가 
    fill_star(n-1,x+2,y+2)

fill_star(N, 0, 0)
for s in stars:
    print(''.join(s))