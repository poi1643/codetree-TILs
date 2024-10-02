n = int(input())

arr = list(map(int, input().split()))

def fun(arr, k, max_):
    if k < 0:
        return max_

    if arr[k] > max_:
        return fun(arr, k-1, arr[k])
        
    else:
        return fun(arr, k-1, max_)
    

print(fun(arr, n-1, 0))