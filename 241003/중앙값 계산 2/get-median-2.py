n = int(input())
arr = list(map(int, input().split()))

blank = []
for i in range(n):
    blank.append(arr[i])
    if i%2 == 0:
        blank = sorted(blank)
        print(blank[i//2], end=' ')