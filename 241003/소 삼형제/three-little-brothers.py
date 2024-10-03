N = int(input())

result = []
num = []
for i in range(N):
    temp = []
    temp_string = ''
    a, b, c = input().split()
    temp.append(a)
    temp.append(b)
    temp.append(c)
    temp.sort()
    for i in temp:
        temp_string += i
    if temp_string not in result:
        result.append(temp_string)
        num.append(1)
    else:
        num[result.index(temp_string)] += 1

print(max(num))