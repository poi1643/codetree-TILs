n = int(input())

arr = list(map(int, input().split()))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return a * b // gcd(a, b)


def find_lcm(arr, n, num):
    if n == 0:
        return lcm(num, arr[n])
    else:
        return find_lcm(arr, n-1, lcm(arr[n], num))

print(find_lcm(arr, n-1, 1))