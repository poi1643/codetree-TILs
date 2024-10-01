n1, n2 = map(int, input().split())
arr_n1 = list(map(int, input().split()))
arr_n2 = list(map(int, input().split()))
flag1 = False
flag2 = False
for i in arr_n1:
    if flag1 == False:
        cnt = 0
    for j in arr_n2:
        if i == j:
            cnt+=1
            flag1 = True
            break

        else: 
            flag1 = False
            break
    if cnt == n2:
        flag2 = True
        break

if flag2:
    print('Yes')
else:
    print('No')