s_ab = int(input())
ma, fab, mb = map(int, input().split())

f_ab_total = ma+fab+mb

if s_ab <= f_ab_total or s_ab <= 240:
    print('high speed rail')
else:
    print('flight')