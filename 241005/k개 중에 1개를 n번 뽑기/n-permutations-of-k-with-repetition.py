k, n = map(int, input().split())
target = ''
for i in range(1, k+1):
    target += str(i)

#print(target)
def print_num(curr_num):
    if len(curr_num) == n:
        for i in curr_num:
            print(i, end=' ')
        return print()
    else:
        for i in target:
            print_num(curr_num + i)
        return

print_num('')