n = int(input())

answer = []

while True:
    if n == 1:
        answer.append(1)
        break
    else:
        answer.append(n%2)
        n //= 2

answer1 =''

for i in answer[::-1]:
    answer1 += str(i)
    #print(i,end='')

print(answer1)