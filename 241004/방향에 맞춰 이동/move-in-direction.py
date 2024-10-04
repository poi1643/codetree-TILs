n = int(input())

pos = [0, 0]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def cal(d):
    if d == 'E':
        return 0
    elif d == 'W':
        return 1
    elif d == 'S':
        return 2
    else:
        return 3

for i in range(n):
    direction, dist = input().split()
    dist = int(dist)
    index = cal(direction)
    pos[0] += dx[index] * dist
    pos[1] += dy[index] * dist

for i in pos[::-1]:
    print(i, end=' ')