# P-position, N-position 기초
import sys
input = sys.stdin.readline

N = int(input())
winner = ['?'] * (N+1)
for i in range(1, N+1):
    if i in [1, 3]:
        winner[i] = 'CY'
    elif i in [2, 4]:
        winner[i] = 'SK'
    else:
        if 'CY' in [winner[i-1], winner[i-3], winner[i-4]]:
            winner[i] = 'SK'
        else:
            winner[i] = 'CY'
print(winner[N])