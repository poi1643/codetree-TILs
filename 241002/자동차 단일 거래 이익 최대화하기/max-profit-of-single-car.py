n = int(input())
arr = list(map(int, input().split()))

max = 0
for i in range(n):
    for j in range(i,n):
        if arr[j]-arr[i] >= max:
            max = arr[j] - arr[i]

print(max)