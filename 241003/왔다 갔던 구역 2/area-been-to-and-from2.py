n = int(input())

result = [0] * 300

for i in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for i in range(1, x):
            result[150-i] += 1
    else:
        for i in range(1, x):
            result[150+i] += 1


ans = 0
for i in result:
    if i > 1:
        ans += 1

print(ans)