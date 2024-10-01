n = int(input())

arr = list(map(int, input().split()))

max = 0
exist = 0

for i in arr:
    if i> max:
        exist = 0
        max = i
    elif i == max:
        exist = 1

if exist == 1:
    print(-1)
else:
    print(max)