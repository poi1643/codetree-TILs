char = input()
before = ''
count = []

for i in char:
    if i != before:
        count.append(i)
        count.append(1)
        before = i
    else:
        count[-1] += 1

result = ''
for i in count:
    result += str(i)

print(len(result))
print(result)