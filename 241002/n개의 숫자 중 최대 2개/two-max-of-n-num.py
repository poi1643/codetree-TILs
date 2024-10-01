n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

print(sorted_arr[-1], sorted_arr[-2])