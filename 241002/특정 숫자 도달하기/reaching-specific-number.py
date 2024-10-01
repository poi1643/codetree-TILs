arr = list(map(int, input().split()))
result = 0
num = 0
flag = False

for i in arr:
    if i<249:
        result += i
        num += 1
    else:
        break

avg = result/float(num)
print('%d %.1f' %(result, avg))