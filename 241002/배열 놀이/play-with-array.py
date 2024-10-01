n, q = map(int, input().split())

arr = list(map(int, input().split()))


for i in range(q):
    question = list(map(int, input().split()))
    if question[0] == 1:
        print(arr[question[1]-1])
        
    elif question[0] == 2:
        flag = 0
        target = question[1]
        for idx, j in enumerate(arr):
            if target == j:
                print(idx+1)
                flag = 1
                break
        if flag == 0:
            print(0)
            
    if question[0] == 3:
        l, m = question[1], question[2]
        for j in range(l-1, m):
            print(arr[j], end =' ')
        print('')