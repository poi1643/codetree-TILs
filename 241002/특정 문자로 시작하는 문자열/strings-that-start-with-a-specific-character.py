n = int(input())

arr = [input() for _ in range(n)]

target = input()

cnt = 0
avg = 0

for i in arr:
    if i[0] == target:
        cnt += 1
        avg += len(i)

print('%d %.2lf' %(cnt, avg/cnt))