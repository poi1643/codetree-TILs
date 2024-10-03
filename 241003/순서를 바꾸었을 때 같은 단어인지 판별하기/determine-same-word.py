a = input()
b = input()
a = list(a)
b = list(b)
a.sort()
b.sort()

if a == b:
    print('Yes')
else:
    print('No')