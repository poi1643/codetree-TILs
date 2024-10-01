a = input()
target = input()
cnt = 0
for i in range(len(a)-1):
    if a[i:i+2] == target:
        cnt += 1

print(cnt)