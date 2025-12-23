# 네 제곱수의 정리의 응용

import sys
input = sys.stdin.readline

N = int(input())

for a in range(int(N ** 0.5), 0, -1):
    third = N - a ** 2
    # 바로 성공하는가?
    if int(third ** 0.5) ** 2 == third:
        print("%d %d %d %d" %(a, int(third ** 0.5), 0, 0))
        sys.exit()

    # 성공이 안 될 경우
    cur = third
    while cur % 4 == 0:
        cur = cur // 4
    if cur % 8 == 7:
        continue
    
    for b in range(int(third ** 0.5), 0, -1):
        second = third - b ** 2
        if int(second ** 0.5) ** 2 == second:
            print("%d %d %d %d" % (a, b, int(second ** 0.5), 0))
            sys.exit()
        
        # second를 정리해아 한다.
        # if second % 4 == 3:
            # continue
        for c in range(int(second ** 0.5), 0, -1):
            d = second - c ** 2
            # d는 제곱수인가?
            if int(d ** 0.5) ** 2 == d:
                print("%d %d %d %d" %(a, b, c, int(d ** 0.5)))
                sys.exit()