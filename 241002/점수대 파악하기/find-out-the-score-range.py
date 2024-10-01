arr = list(map(int, input().split()))

score = [0]*11

for i in arr:
    if i == 0:
        break;
    if i >= 10:
        score[i//10] += 1
    else:
        continue

for i in range(10, 0, -1):
    print('%d - %d' %(i*10, score[i]))