n = int(input())

status = [0] * 1000000
black = [0] * 1000000
white = [0] * 1000000
place = 500000
for i in range(n):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'L':
        for i in range(x):
            status[place - i] = 1
            white[place - i] += 1
        place -= (x-1)
    else:
        for i in range(x):
            status[place + i] = 2
            black[place + i] += 1
        place += (x-1)

gray_count = 0
white_count = 0
black_count = 0
for i in range(1000000):
    if(white[i] >1 and black[i] > 1):
        status[i] = 0
        gray_count += 1
    elif status[i] == 1:
        white_count += 1
    elif status[i] == 2:
        black_count += 1

print(white_count, black_count, gray_count)