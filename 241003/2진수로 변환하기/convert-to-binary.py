n = int(input())
answer = []

while True:
    if n < 2:
        answer.append(n)
        break
    else:
        answer.append(n%2)
        n //= 2

for i in answer[::-1]:
    print(i,end='')