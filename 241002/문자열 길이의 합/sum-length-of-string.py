n = int(input())

arr = [input() for _ in range(n)]

cnt = 0
result = 0
for i in arr:
    result += len(i)
    if i[0] == 'a':
        cnt += 1

print(result, cnt)