# 5의 배수를 맞으면 확실히 짐
# 5k + 2 를 줄 경우, 5K + 3이나 5k+ 1로 가는데
# 5k + 1의 경우는 상대에게 5k를 넘길 수 있음
# 5k + 3의 경우는 # 5k + 2 형태를 상대에에게 줌..
# 반복해..상대가 2개 맞으면 내 승리...로 5k+2도 패배패턴
# 이게 되는 이유는 4^k 형태는 1, 4 나머지 뿐이라.

import sys
input = sys.stdin.readline

N = int(input())

if N % 5 in [1, 3, 4]:
    print('SK')
else:
    print('CY')