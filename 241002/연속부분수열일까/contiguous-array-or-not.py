n1, n2 = map(int, input().split())
arr_n1 = list(map(int, input().split()))
arr_n2 = list(map(int, input().split()))
cnt = 0

for i in range(n1):
    cnt = 0
    
    if(arr_n1[i] == arr_n2[0] and n1-i>=n2):
        for k in range(n2):
            if(arr_n1[i+k] == arr_n2[k]):
                cnt += 1
            else:
                break
    if cnt == n2:
        break
    
if cnt == n2:
    print('Yes')
else:
    print('No')