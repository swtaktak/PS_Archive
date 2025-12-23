import sys
input = sys.stdin.readline
# 원주각의 성질에 의거함
# 원주각이 180도 -> 실제 대각은90도
# 대칭인 두 점에 대해서, 나머지 모두 선택해야함
# N(N-2) // 2
# 따라서, 이게 가능할려면 짝수여야함.

T = int(input())
for _ in range(T):
    N = int(input())
    
    if N % 2 == 1:
        print(0)
    else:
        print(N * (N-2) // 2)