n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = 0
for i in a:
    if i not in b:
        flag = 1
        break

if flag == 0:
    print('Yes')
else:
    print('No')