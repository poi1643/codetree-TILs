month1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


Y, M, D = map(int, input().split())

def if_yun(Y):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False

def print_season(M):
    if M <3:
        print('Winter')
    elif M < 6:
        print('Spring')
    elif M < 9:
        print('Summer')
    elif M < 12:
        print('Fall')
    else:
        print('Winter')


if if_yun(Y):
    if month2[M-1] < D:
        print(-1)
    else:
        print_season(M)
else:
    if month1[M-1] < D:
        print(-1)
    else:
        print_season(M)