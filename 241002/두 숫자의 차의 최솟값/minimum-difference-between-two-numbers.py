n = int(input())
arr = list(map(int, input().split()))

min = 100
for i in range(n-1):
    for j in range(i+1,n):
        if abs(arr[j]-arr[i]) < min:
            min = abs(arr[j]-arr[i])

print(min)