n, m = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1

for i in grid:
    for j in i:
        print(j, end=' ')
    print()