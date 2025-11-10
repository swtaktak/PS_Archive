import sys
input = sys.stdin.readline
# N이냐 N(N+1) 형태냐

T = int(input())
for _ in range(T):
    N = int(input())
    
    # case1 : 정사각형 (N^2)
    s1 = int(N ** 0.5)
    
    while s1 ** 2 < N:
        s1 += 1
    a1 = s1 * 4
    
    s2 = int(N ** 0.5) - 1
    
    while s2 * (s2 + 1) < N:
        s2 += 1
    a2 = s2 * 4 + 2
    
    print(min(a1, a2))