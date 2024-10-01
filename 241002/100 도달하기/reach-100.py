n = int(input())

arr = [1, 5]
index = 2
while True:
    a = arr[index-1] + arr[index -2]
    if a >= 100:
        arr.append(a)
        break
    else:
        arr.append(a)
        index += 1

for i in arr:
    print(i, end = ' ')