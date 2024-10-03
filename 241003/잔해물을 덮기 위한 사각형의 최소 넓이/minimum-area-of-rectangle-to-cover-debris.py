result = [[0]* 2200 for _ in range(2200)]
x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        result[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        result[i][j] = 0


max_x = 0
max_y = 0
min_y = 10000
min_x = 10000
flag = 0
for i in range(2200):
    for j in range(2200):
        flag = 1
        if result[i][j] == 1:
            if i < min_x:
                min_x = i
            elif i > max_x:
                max_x = i
            
            if j < min_y:
                min_y = j
            elif j > max_y:
                max_y = j

#print(max_x, min_x, max_y, min_y)
if flag == 0:
    print(0)
else:
    print((max_x - min_x)*(max_y - min_y))