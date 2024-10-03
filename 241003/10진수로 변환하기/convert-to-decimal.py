n = input()
num = 0
for i in n:
    a = num * 2
    num = a + int(i)
    #num += ((num * 2) + int(i))
    

print(num)