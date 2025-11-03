# 이게 무조건 4 이상이 나올 수가 없다.
# 그리고 3이 나온 순간 3은 확정이다.
# 1 11 12 1121 122111 112213 # 끝

import sys
input = sys.stdin.readline

N = int(input())

if N >= 6:
    print(3)
elif N >= 3:
    print(2)
else:
    print(1)