bowl = input()
n = len(bowl)
height = 10

for i in range(1, n):
    if bowl[i-1] != bowl[i]:
        height += 10
    else:
        height += 5

print(height)