N, T = map(int, input().split())

inst = input()

arr = [list(map(int, input().split())) for _ in range(N)]


direction = [-1, 0]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
da, db = ['북', '동', '남', '서'], ['북', '동', '남', '서']

index = 0 #방향을 나타냄
r, c = N//2  , N // 2 

score = arr[r][c]


def is_valid(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


for i in inst:
    
    if i == 'R':
        index += 1
        #print(da[index%4], db[index%4])
    elif i == 'L':
        index -= 1
        #print(da[index%4], db[index%4])
    elif i == 'F':
        new_x = r + dx[index%4]
        new_y = c + dy[index%4]
        if is_valid(new_x, new_y):
            r, c = new_x, new_y
        
            score += arr[r][c]




print(score)
#print(5 + 6 + 3+ 2)