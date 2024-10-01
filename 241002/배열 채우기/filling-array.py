arr = list(map(int, input().split()))

index = arr.index(0)
if index != None:
    for i in range(index-1, -1 ,-1):
        print(arr[i], end =' ')
else:
    for i in arr[::-1]:
        print(i, end = '')