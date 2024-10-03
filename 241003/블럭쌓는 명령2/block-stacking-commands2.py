N, K = map(int, input().split())
result = [0] * (N+1)

for i in range(K):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        result[i] += 1

print(max(result))