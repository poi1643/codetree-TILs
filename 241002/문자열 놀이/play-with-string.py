s, q = input().split()

s = list(s)

for i in range(int(q)):
    n, a, b = input().split()
    if n == '1':
        temp = s[int(a)-1]
        s[int(a)-1] = s[int(b)-1]
        s[int(b)-1] = temp
        k = ''.join(s)
        print(k)
    elif n == '2':
        k = ''.join(s)
        k = k.replace(a,b)
        print(k)
    s = list(k)