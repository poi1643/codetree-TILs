n = input()
if n == '1':
    print(0)
else:

    n = list(n)

    for i in range(1, len(n)):
        if n[i] == '0':
            n[i] = '1'
        break

    n = str(''.join(n))

    n = int(n,2)

    print(n)