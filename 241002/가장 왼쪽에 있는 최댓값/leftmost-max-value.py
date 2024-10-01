n = int(input())

arr = list(map(int, input().split()))
result = []

while True:
    if len(arr)>=2:
        a = arr.index(max(arr))
        result.append(arr.index(max(arr)))
        arr = arr[0:a]
    else:
        break

for i in result:
    print(i+1, end=' ')