n, m = map(int, input().split())  # n: 열의 크기, m: 행의 크기

arr1 = [list(map(int, input().split())) for _ in range(m)]  # 첫 번째 배열 입력 받기
arr2 = [list(map(int, input().split())) for _ in range(m)]  # 두 번째 배열 입력 받기

result = [[1]*n for _ in range(m)]  # 결과 배열을 1로 초기화

# 배열 요소를 비교하여 동일하면 0으로 설정
for i in range(m):  # 행의 크기 m 만큼 반복
    for j in range(n):  # 열의 크기 n 만큼 반복
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))