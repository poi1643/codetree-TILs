a = input()
b = len(a)

if b % 2 == 0:
    for i in a[-1:-b:-2]:
        print(i, end='')
else:
    for i in a[-2:-b:-2]:
        print(i, end='')