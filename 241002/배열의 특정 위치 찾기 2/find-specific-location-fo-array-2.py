arr = list(map(int, input().split()))

odd = 0
even = 0

for i in arr[0::2]:
    odd += i

for j in arr[1::2]:
    even += j

print(abs(odd-even))