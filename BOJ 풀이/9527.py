import sys
import math
input = sys.stdin.readline

def onecnt(x):
    if x <= 0:
        return 0
    else:
        cur_digit = (x + 1).bit_length()-1
        # 정확하게 개수가 맞다면
        cutline = (2 ** cur_digit) - 1
        if x == cutline:
            # 2의 거듭제곱형태 까지는 0, 1 개수가 모두 동일함
            return cur_digit * (2 ** cur_digit) // 2
        else:
            new_x = x - cutline
            return onecnt(new_x - 1) + new_x + cur_digit * (2 ** cur_digit) // 2

A, B = map(int, input().split())
answer = onecnt(B) - onecnt(A-1)
print(answer)