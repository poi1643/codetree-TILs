n = int(input())

status = 0
result = []
cnt = 1

for i in range(n):
    if n == 1:
        result.append(cnt)
    elif i == 0:
        before = int(input())
        if before > 0:
            status = 0
    else:
        a = int(input())
        if before * a > 0:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
            before = a

result.append(cnt)

print(max(result))