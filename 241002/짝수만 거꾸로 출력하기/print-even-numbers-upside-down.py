n = int(input())
arr = list(map(int, input().split()))

Wkrtn = []
for i in arr:
    if i %2 == 0:
        Wkrtn.append(i)

for j in Wkrtn[::-1]:
    print(j, end = ' ')