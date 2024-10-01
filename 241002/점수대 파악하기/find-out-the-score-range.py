arr = list(map(int, input().split()))

score = [0]*11

for i in arr:
    if arr == 0:
        break;
    else:
        score[i//10] += 1

for i in range(10, 0, -1):
    print('%d - %d' %(i*10, score[i]))