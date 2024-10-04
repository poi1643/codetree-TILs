n = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = []

cases = [[0,1,2], [0,1,-1],[0,-1,-2],[-3,-2,-1]]
for i in cases:
    num = 1
    for j in i:
        num *= arr[j]
    result.append(num)

print(max(result))