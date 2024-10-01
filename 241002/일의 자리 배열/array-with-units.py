a, b = map(int, input().split())
arr = [a, b]
for i in range(3, 11):
    arr.append(arr[i-3] + arr[i-2])

for i in arr:
    print(str(i)[-1], end =' ')