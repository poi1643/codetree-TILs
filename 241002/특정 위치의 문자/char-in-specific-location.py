arr = ['L','E','B','R','O','S']

flag = 0
target = input()
for idx, i in enumerate(arr):
    if i == target:
        print(idx)
        flag = 1
        break
if flag == 0:
    print('None')