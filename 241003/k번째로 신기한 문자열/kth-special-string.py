n, k, T = input().split()

n = int(n)
k = int(k)
length = len(T)
answer = []

for i in range(n):
    q = input()
    if q[0:length] == T:
        answer.append(q)

print(sorted(answer)[k-1])