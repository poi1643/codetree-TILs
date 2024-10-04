n = input()
print(n)

for i in range(len(n)):
    n = n[-1] + n[:len(n)-1]
    print(n)