n = int(input())

result =[0]*300
for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 101
    x2 += 101
    for i in range(x1, x2):
        result[i] += 1

print(max(result))