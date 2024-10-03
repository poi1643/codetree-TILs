a, b, c = map(int, input().split())

point = 11 * 24 * 60 + 11 * 60 + 11

target = a * 24 * 60 + b * 60 + c


if target < point:
    print(-1)
else:
    print(target - point)