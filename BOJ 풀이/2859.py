import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def str_to_min(s):
    h, m = s.split(":")
    return 60 * int(h) + int(m)

s1 = str(input().rstrip())
s2 = str(input().rstrip())
i1 = str(input().rstrip())
i2 = str(input().rstrip())

s1_m = str_to_min(s1)
i1_m = str_to_min(i1)
s1_set = set()

s2_m = str_to_min(s2)
i2_m = str_to_min(i2)
s2_set = set()

lcm_star = i1_m * i2_m // gcd(i1_m, i2_m)

cutline = max(s1_m, s2_m) + lcm_star

for i in range(s1_m, cutline + 1, i1_m):
    s1_set.add(i)
    
for i in range(s2_m, cutline + 1, i2_m):
    s2_set.add(i)
    
twostar = list(s1_set & s2_set)
if len(twostar) == 0:
    print('Never')
else:
    mintime = min(twostar)
    days = (mintime // 1440) % 7
    rmd = mintime % 1440
    
    day_dict = {0:'Saturday', 1:'Sunday', 2:'Monday',
                3:'Tuesday', 4:'Wednesday', 5:'Thursday',
                6:'Friday'}
    print(day_dict[days])
    
    rh, rm = str(rmd // 60), str(rmd % 60)
    
    if len(rh) == 1:
        rh = '0' + rh
    if len(rm) == 1:
        rm= '0' + rm
    print(rh + ':' + rm)