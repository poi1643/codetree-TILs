a = input()

cnt = 0

for i in range(len(a)-1):
    if a[i:i+2] == 'ee':
        cnt += 1
print(cnt, end=' ')

cnt = 0

for i in range(len(a)-1):
    if a[i:i+2] == 'eb':
        cnt += 1

print(cnt)