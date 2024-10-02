N = int(input())
global result
def f(n, result):

    if n < 10:
        result += n **2
        return result
    else:
        result += (n%10)**2
        return f(n//10, result)

print(f(N, 0))