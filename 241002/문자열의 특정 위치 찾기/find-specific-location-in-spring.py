a, b = map(str, input().split())

c = a.find(b)

if c == -1:
    print('No')
else:
    print(c)