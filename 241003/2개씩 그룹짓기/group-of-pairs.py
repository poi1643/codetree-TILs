n = int(input())
arr = list(map(int, input().split()))

num = len(arr)
max = 0
min = 2000
arr.sort()
for i in range(n):
    temp = arr[i] + arr[-(i+1)]
    if max < temp:
        max = temp
    

print(max)