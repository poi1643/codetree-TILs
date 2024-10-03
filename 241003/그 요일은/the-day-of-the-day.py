m1, d1, m2, d2 = map(int, input().split())
target = input()
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


a = day.index(target)

target1 = 0
target2 = 0
for i in range(m2):
    target1 += month[i]

target1 += d2

for i in range(m1):
    target2 += month[i]
target2 += d1


num = target1 - target2


result = num // 7
if (num % 7 >= a):
    result += 1

print(result)