N, A, B = map(int, input().split())

s_list = [0] * 10000
NS_list = [0] * 10000

for i in range(N):
    q, n = input().split()
    n = int(n) - 1
    if q == 'S':
        s_list[n] = 1
    else:
        NS_list[n] = 1


result = [0] * 10000

def find_lefts(num, cnt):
    if s_list[num] == 1:
        return cnt
    elif num == A:
        return 1000000000
    else:
        return find_lefts(num-1, cnt+1)

def find_rights(num, cnt):
    if s_list[num] == 1:
        return cnt
    elif num == B:
        return 1000000000
    else:
        return find_rights(num+1, cnt+1)


def find_leftns(num, cnt):
    if NS_list[num] == 1:
        return cnt
    elif num == A:
        return 1000000000
    else:
        return find_leftns(num-1, cnt+1)

def find_rightns(num, cnt):
    if NS_list[num] == 1:
        return cnt
    elif num == B:
        return 1000000000
    else:
        return find_rightns(num+1, cnt+1)


ans = 0
for i in range(A, B+1):
    if min(find_lefts(i, 0), find_rights(i, 0)) >= min(find_leftns(i, 0), find_rightns(i, 0)):
        ans += 1


print(ans)