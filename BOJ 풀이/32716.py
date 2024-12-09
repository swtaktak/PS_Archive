import sys
input = sys.stdin.readline
# 홀수 실패! 다시 계산 해야함.
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
elif N == 4:
    print(1)
elif N == 5:
    print(1)
else:
    if N % 4 == 0:
        print(four_k(N))
    elif N % 4 == 1:
        print(four_k(N-1) + 1)
    elif N % 4 == 2:
        print(four_k_plus_2(N))
    else:
        print(four_k_plus_2(N-1)+1)