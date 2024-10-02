N, S = map(int, input().split())

arr = list(map(int, input().split()))

all = sum(arr)
a = 0
b = 0
result = 100000
for i in range(N):
    for j in range(i+1,N):
        excluded = arr[i] + arr[j]
        if abs(all - excluded) < result:
            result = all - excluded

print(abs(S - result))