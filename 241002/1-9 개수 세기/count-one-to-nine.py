n = int(input())
arr = list(map(int, input().split()))


arr_count =[0] * 9

for i in arr:
    arr_count[i-1] += 1

for i in range(9):
    print(arr_count[i])