m1, d1, m2, d2 = map(int, input().split())

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

target1 = 0
target2 = 0
for i in range(m2):
    target1 += month[i]

target1 += d2

for i in range(m1):
    target2 += month[i]
target2 += d1


num = target1 - target2


if d1 == 9:
    print(num)
print(day[num%7])
'''
if num < 0:
    print(day[(num-1)%7])
else:
    print(day[num%7])
    '''