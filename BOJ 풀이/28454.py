import sys
input = sys.stdin.readline

today = str(input().rstrip())
able = 0
gifts = int(input())
for _ in range(gifts):
    cur_day = str(input().rstrip())
    if cur_day >= today:
        able += 1
print(able)