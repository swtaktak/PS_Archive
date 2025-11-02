import sys
import math
input = sys.stdin.readline

def get_digit(cnt):
    val = 0
    for i in range(9000, 0, -cnt):
        val += math.log10(i)
    return (int(val) + 1)

T = int(input())
for t_case in range(1, T+1):
    cutline = int(input())
    if cutline <= 4:
        print('Case #%d: ...' %(t_case))
    else:
        start = 1
        end = 9000
        ans = 9001
        
        while start <= end:
            mid = (start + end) // 2
            digit = get_digit(mid)
            if digit >= cutline:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        print('Case #%d: IT\'S OVER 9000'%(t_case) + ('!' * ans) )