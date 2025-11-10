# 근과 계수와의 관계를 다루는 문제
# 양수의 경우에는 근 -1을 추가 부여,  음수의 경우에는 근 1을 추가 부여
# 이러면 합, 곱이 커트라인을 넘지 않으며 무조건 방정식을 찾을 수 있다.

import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    
    N = int(input())
    
    if N > 0 and N != 1:
        a = 1
        b = (N - 1) * -1
        c = N * -1
        
    elif N < 0 and N != -1:
        a = 1
        b = (N + 1) * -1
        c = N
        
    elif N == 1:
        a = 1
        b = -2
        c = 1
        
    else:
        a = 1
        b = 2
        c = 1
    
    print("%d %d %d"%(a, b, c))