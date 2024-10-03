# m이 가로, n이 세로
# r이 가로, c가 세로
n, m = map(int, input().split())

block = [[0]*m for _ in range(n)]
arr = list(map(int, input().split()))


#print(block)

cnt = 0
for i in arr:
    for j in range(i):
        block[j][cnt] = 1
    cnt += 1
    

def find_left_wall(r, c):
    if r == 0:
        return False
    else:
        if block[c][r-1] == 1:
            return True
        else:
            return find_left_wall( r-1, c)

def find_right_wall(r, c):
    if r == m-1:
        return False
    else:
        if block[c][r+1] == 1:
            return True
        else:
            return find_left_wall(r+1, c)

for i in range(m):
    for j in range(n):
        if block[j][i] == 0:
            if find_left_wall(i, j) and find_right_wall(i, j):
                block[j][i] = 2




'''
for i in range(m):
    for j in range(n):
        if block[j][i] != 1:
            if find_left_wall(block, i, j) and find_right_wall(block, i, j):
                block[j][i] = 2
'''

    

ans = 0
for i in block:
    ans += i.count(2)
print(ans)