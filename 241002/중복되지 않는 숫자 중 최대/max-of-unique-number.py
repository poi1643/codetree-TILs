n = int(input())

arr = list(map(int, input().split()))

only_one = []
set_arr = set(arr)
for i in set_arr:
    if arr.count(i) == 1:
        only_one.append(i)

if len(only_one) != 0:
    print(max(only_one))
else:
    print(-1)