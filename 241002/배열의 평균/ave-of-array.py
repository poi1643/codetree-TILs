arr = [list(map(int, input().split())) for _ in range(2)]

all_sum = 0
for i in arr:
    print(sum(i)/4, end =' ')
print('')
for i in range(4):
    result = 0
    for j in range(2):
        result += arr[j][i]
    print(result/2, end=' ')
    all_sum += result
print('')
print(all_sum/8)