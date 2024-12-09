import sys
input = sys.stdin.readline

def four_k(N):
    # 다이아몬드가 최대치
    side = N // 4
    return 2 * (side ** 2) - 2 * side + 1
def four_k_plus_2(N):
    side = N // 4
    return 2 * (side ** 2)


N = int(input())
if N <= 3:
    print(0)
else:
    if N % 4 == 0:
        print(four_k(N))
    elif N % 4 == 1:
        print(four_k_plus_2(N+1) - ((N+1) // 4))
    elif N % 4 == 2:
        print(four_k_plus_2(N))
    else:
        print(four_k(N+1) - ((N+1) // 4))