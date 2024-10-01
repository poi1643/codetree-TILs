arr = ["apple", "banana", "grape", "blueberry", "orange"]

target = input()
cnt = 0
for i in arr:
    if i[3] == target or i[2] == target:
        print(i)
        cnt += 1
print(cnt)