arr = list(map(int, input().split()))
result = 0
for i in arr[1::2]:
    result += i
print(result, end=' ')
cnt = 0
result = 0
for j in arr[2::3]:
    result += j
    cnt += 1

avg = result/cnt
print('%.1f'% avg)