def down(n):
    if n != 0:
        for _ in range(n):
            print('*', end =' ')
        if n != 1:
            print()
        down(n-1)


def up(k, n):
    if k != n:
        for _ in range(k):
            print('*', end =' ')
        print()
        up(k+1, n)

def print_star(n):
    down(n)
    up(0, n+1)

n = int(input())    

print_star(n)