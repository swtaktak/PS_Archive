# 7주기이다. 7개마다 승 패가 돌아온다.
import sys
input = sys.stdin.readline
win_dict = {0 : 'CY', 1 : 'SK', 2 : 'CY', 3 : 'SK', 4 : 'SK', 5 : 'SK', 6 : 'SK'}
N = int(input())
print(win_dict[N % 7])