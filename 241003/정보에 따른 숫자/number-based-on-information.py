import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = int(data[1])
    B = int(data[2])
    
    positions = []
    for i in range(N):
        label = data[3 + 2*i]
        p = int(data[4 + 2*i])
        positions.append( (p, label) )
    
    # 모든 위치를 오름차순으로 정렬
    positions.sort()
    
    total_count = 0
    
    for i in range(N):
        p_i, label_i = positions[i]
        
        # 현재 위치의 왼쪽 경계 계산
        if i == 0:
            left_bound = -float('inf')
        else:
            p_prev, _ = positions[i-1]
            left_bound = (p_prev + p_i) // 2 + 1
        left_bound = max(left_bound, A)
        
        # 현재 위치의 오른쪽 경계 계산
        if i < N-1:
            p_next, _ = positions[i+1]
            right_bound = (p_i + p_next) // 2
        else:
            right_bound = float('inf')
        right_bound = min(right_bound, B)
        
        # 현재 위치가 S인 경우, [left_bound, right_bound] 범위 내의 숫자를 포함
        if label_i == 'S':
            if left_bound <= right_bound:
                total_count += (right_bound - left_bound + 1)
        
        # 두 위치 간의 중간점이 정수인 경우 처리
        if i < N-1:
            if (p_i + positions[i+1][0]) % 2 == 0:
                x = (p_i + positions[i+1][0]) // 2
                # x가 [A, B] 범위 내에 있고, S가 포함된 경우에만 포함
                if A <= x <= B and (label_i == 'S' or positions[i+1][1] == 'S'):
                    # S가 이미 영향을 미치는 범위에 포함된 경우 중복 포함 방지
                    if label_i != 'S' and positions[i+1][1] == 'S':
                        total_count += 1
    
    print(total_count)

if __name__ == "__main__":
    main()