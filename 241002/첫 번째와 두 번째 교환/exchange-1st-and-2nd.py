a = input()
a = list(a)

first = a[0]
second = a[1]
for i in range(len(a)):
    if a[i] == first:
        a[i] = second
    elif a[i] == second:
        a[i] = first
    
a = ''.join(a)
print(a)