# 점화식으로 풀어보자...
# an = 2/3(1-(-0.5)^n)
import sys
import math
input = sys.stdin.readline
N = int(input())
log_2 = math.log10(2)

# 홀짝 따라 달라짐
# n이 홀수인 경우. 커지는 부분에 대해 분모가 달라져.. 차수 하나 컷트.
if N % 2 == 1:
    N -= 1
answer = int(N * log_2)
print(answer)