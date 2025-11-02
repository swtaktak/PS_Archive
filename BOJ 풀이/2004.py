import sys
input = sys.stdin.readline


def count_two(n):
    cnt = 0
    cur = 2
    while cur <= n:
        cnt += (n // cur)
        cur *= 2
    return cnt

def count_five(n):
    cnt = 0
    cur = 5
    while cur <= n:
        cnt += (n // cur)
        cur *= 5
    return cnt

N, M = map(int, input().split())
num_2 = count_two(N) - count_two(N-M) - count_two(M)
num_5 = count_five(N) - count_five(N-M) - count_five(M)

print(min(num_2, num_5))