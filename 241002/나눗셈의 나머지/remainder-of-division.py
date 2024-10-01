a, b = map(int, input().split())
result = [0] * (b+1)

while True:
    c = a % b
    a = int(a // b)

    result[c] += 1
    if a < 1:
        break

k = 0
for i in result:
    k += i ** 2


print(k)