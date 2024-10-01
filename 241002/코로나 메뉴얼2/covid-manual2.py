arr = [list(input().split()) for _ in range(3)]

result = [0, 0, 0, 0]

for i in arr:
    if i[0] == 'Y' and int(i[1]) >= 37:
        result[0] += 1
    elif i[0] == 'N' and int(i[1]) >= 37:
        result[1] += 1
    elif i[0] == 'Y' and int(i[1]) < 37:
        result[2] += 1
    else:
        result[3] += 1

for i in result:
    print(i, end=' ')

if result[0] >= 2:
    print('E')