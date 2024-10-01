n = int(input())
cnt = 1
flag = 0
while True:
    print(n * cnt, end =' ')
    cnt += 1
    if n * cnt % 5 == 0:
        flag += 1
        if flag == 2:
            print(n*cnt)
            break