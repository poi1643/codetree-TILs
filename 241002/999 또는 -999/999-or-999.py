arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == -999 or i == 999:
        break
    else:
        cnt += 1

print(max(arr[0:cnt]), min(arr[0:cnt]))