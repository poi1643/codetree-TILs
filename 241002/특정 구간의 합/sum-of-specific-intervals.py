n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum(n_arr[a1-1:a2]))