def fun(N):
    if N == 0:
        return
    print(N,end =' ')
    fun(N-1)
    print(N, end =' ')

N = int(input())

fun(N)