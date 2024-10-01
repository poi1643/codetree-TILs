arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 0:
        break;
    else:
        cnt+=1
        

result = sum(arr[0:cnt])
avg = result/(cnt)

print('%d %.1f' %(result, avg))