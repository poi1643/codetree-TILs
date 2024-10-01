arr = list(map(int, input().split()))

min = 1001
max = 0

for i in arr:
    if i<500 and i>max:
        max = i
    elif i>500 and i<min:
        min = i

print(max, min)