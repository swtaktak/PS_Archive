# 2를 계속 곱해 나간다 언제 절댓값을 초과하는가?
# 홀수의 경우 모두 다 표현된다!
import sys
input = sys.stdin.readline
N = int(input())
if N == 0:
    print(0)
elif N % 2 == 0:
    print(-1)
else:
    # 2진법 길이
    bins = ''
    num = abs(N)
    while num > 0:
        bins += str(num % 2)
        num = num // 2
    print(len(bins))