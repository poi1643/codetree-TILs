k, n = map(int, input().split())
target = ''
for i in range(1, k+1):
    target += str(i)

def print_num(curr_num):
    if len(curr_num) == n:
        for i in curr_num:
            print(i, end =' ')
        return print()
    else:
        for i in target:
            if len(curr_num) > 2:
                if curr_num[-1] == curr_num[-2] == i:
                    continue
            else:
                print_num(curr_num + i)
        return

if k == 1:
    if n < 3:
        print_num('')
else:
    print_num('')