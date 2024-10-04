n, m = map(int, input().split())

ans = [1]
for i in range(m):
    a, b = map(int, input().split())
    if a in ans and b not in ans:
        ans.append(b)
    elif b in ans and a not in ans:
        ans.append(a)

print(len(ans) - 1)