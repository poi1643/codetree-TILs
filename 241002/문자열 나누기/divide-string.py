n = int(input())
arr = list(map(int, input().split()))

b = ''
for i in arr:
    b += str(i)

for i in range(0,len(b),5):
    print(b[i:i+5])