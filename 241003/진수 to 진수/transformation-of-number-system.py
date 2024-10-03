a, b = map(int, input().split())
n = input()
n = int(n, a)

result = []

while True:
    if n < b:
        result.append(n)
        break
    else:
        result.append(n%b)
        n //= b

for i in result[::-1]:
    print(i,end='')