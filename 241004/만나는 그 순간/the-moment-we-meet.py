n, m = map(int, input().split())

a_status = [0]
b_status = [0]



end_time = 1
for i in range(1, n+1):
    d, t = input().split()
    t = int(t)
    
    start_time = end_time
    end_time = start_time + t
    if d == 'R':
        for j in range(start_time, end_time):
            a_status.append(a_status[j-1] + 1)
    else:
        for j in range(start_time, end_time):
            a_status.append(a_status[j-1] - 1)

end_time = 1
for i in range(1, m+1):
    d, t = input().split()
    t = int(t)
    start_time = end_time
    end_time = start_time + t
    if d == 'R':
        for j in range(start_time, end_time):
            b_status.append(b_status[j-1] + 1)
    else:
        for j in range(start_time, end_time):
            b_status.append(b_status[j-1] - 1)


x, y = len(a_status), len(b_status)
for i in range(abs(x - y)):
    if x <= y:
        a_status.append(2000)
    else:
        b_status.append(2000)
flag = 0
for i in range(1, max(x, y)+1):
    if a_status[i] == b_status[i]:
        print(i)
        flag = 1
        break

if flag == 0:
    print(-1)