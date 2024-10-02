N, S = map(int, input().split())

arr = list(map(int, input().split()))

all_ = sum(arr)

result = 100000
for i in range(N):
    for j in range(i+1,N):
        excluded = arr[i] + arr[j]
        remained = all_ - excluded
        
        if abs(S-remained) < abs(result-S):
            #print(remained)
            result = remained


print(abs(S - result))