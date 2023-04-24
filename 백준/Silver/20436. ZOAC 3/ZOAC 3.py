# 손이 위치한 알파벱 입력받기 
l, r = map(str, input().split())
string = input()

# 키보드가 생긴 모양에 따라 keyboard 리스트 생성하기 
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'
xl, yl, xr, yr = '0', '0', '0', '0'

# 손 위치의 좌표 저장하기 
for i in range(len(keyboard)):
    if l in keyboard[i]:
        xl, yl = i, keyboard[i].index(l)

    if r in keyboard[i]:
        xr, yr = i, keyboard[i].index(r)

dap = 0

for s in string:
    # 각 문자마다 누르는 시간은 1만큼 소요되기 때문에
    # 입력하려고 하는 문자열을 순회하면서 ans + 1을 해준다
    dap += 1
    # 입력하려는 문자 s가 모음 리스트에 있을 때
    # 오른손에 해당하는 좌표로부터 누르려는 키까지의 거리를 계산하여 dap에 더해줌
    if s in mo:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)

                dap += abs(xr-nx) + abs(yr-ny)

                xr, yr = nx, ny
                break

    # 입력하려는 문자 s가 모음 리스트에 없을 때
    # 왼손에 해당하는 좌표로부터 누르려는 키까지의 거리를 계산하여 ans에 더해줌
    else:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)

                dap += abs(xl-nx) + abs(yl-ny)

                xl, yl = nx, ny
                break

print(dap)