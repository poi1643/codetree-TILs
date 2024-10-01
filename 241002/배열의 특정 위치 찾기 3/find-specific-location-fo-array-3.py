arr = list(map(int, input().split()))
n = len(arr)
for i in range(3, n):
    result = arr[i-3] + arr[i-2] + arr[i-1]
    if arr[i] == 0:
        break

print(result)