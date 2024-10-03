n = int(input())
arr = list(map(int, input().split()))

num = len(arr)
max = 0
min = 2000
for i in range(num):
    for j in range(i+1, num):
        temp = arr[i] + arr[j]
        if max < temp:
            max = temp
    if max < min:
        min = max
print(min)