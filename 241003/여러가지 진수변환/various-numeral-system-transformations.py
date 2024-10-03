N, B = map(int, input().split())

result = []

while True:
    if N < B:
        result.append(N)
        break
    else:
        result.append(N%B)
        N //= B

for i in result[::-1]:
    print(i, end='')