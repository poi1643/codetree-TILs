a = input()
b = input()
c = input()

a1 = abs(len(a) - len(b))
b1 = abs(len(b) - len(c))
c1 = abs(len(c) - len(a))

print(max(a1, b1, c1))