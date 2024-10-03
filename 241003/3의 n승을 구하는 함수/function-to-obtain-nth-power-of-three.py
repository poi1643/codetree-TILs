n = int(input())

def print_3(num, n):
    if n == 0:
        print(num)
        return
    else:
        return print_3(num*3, n-1)

print_3(1, n)