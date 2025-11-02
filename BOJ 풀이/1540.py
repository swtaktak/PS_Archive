import sys
input = sys.stdin.readline
# idea  N^2 형태나 N(N+1) 형태로 답을 구한다.
# 여남은 거는 

def n_square(n):
    return ((n-1) * n * (2*n-1))//6
def n_rectangle(n):
    return n_square(n) + (n-1) * n // 2
def remainder(r):
    return (r-1) * r // 2

N = int(input())
side = int(N ** 0.5)
if side ** 2 + side <= N:
    rmd = N - (side ** 2 + side)
    answer = n_rectangle(side) + remainder(rmd)
else:
    rmd = N - (side ** 2)
    answer = n_square(side) + remainder(rmd)
print(answer)