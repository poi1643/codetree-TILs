n = input()

if n == '1':
    print(0)
elif '0' not in n:
    print(int(n,2) - 1)

else:
    n = list(n)

    for i in range(1, len(n)):  # 처음 만난 0을 1로 바꾸는 코드
        if n[i] == '0':
            n[i] = '1'
            break  # 첫 번째 0을 1로 바꾼 후 반복 중단
           
    n = ''.join(n)
    n = int(n, 2)

    print(n)