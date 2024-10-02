N, H, T = map(int, input().split())

arr = list(map(int, input().split()))

cost = 20000

for i in range(N-T+1):
    temp = 0
    for j in range(T):
        temp += abs(H - arr[i+j])
    if temp <= cost:
        cost = temp

print(cost)