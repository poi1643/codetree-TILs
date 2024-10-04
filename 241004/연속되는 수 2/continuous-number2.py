n = int((input()))

cnt = 0
result = []
for i in range(n):
    if i == 0:
        before = int(input())
        cnt += 1
    else:
        a = int(input())
        if a != before:
            result.append(cnt)
            cnt = 1
            before = a
        else:
            cnt += 1


print(max(result))