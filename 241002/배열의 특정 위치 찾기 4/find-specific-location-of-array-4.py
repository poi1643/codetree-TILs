arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 0:
        break
    else:
        cnt +=1

result = 0
num = 0
for i in arr[0:cnt]:
    if i % 2 == 0:
        result += i
        num += 1

print(num, result)