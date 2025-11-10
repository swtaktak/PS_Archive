import sys
input = sys.stdin.readline
# idea : 더블 카운팅
# 각 음식 입장에서 몇 번이 최대이고, 몇 번이 최소인가?
# 빠른 곱셈 코드 활용
P = 1000000007
def fast_pow(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        half_val = fast_pow(a, b // 2, c)
        if b % 2 == 0:
            return (half_val * half_val) % c
        else:
            return (half_val * half_val * (a%c)) % c
        
food = int(input())
sco_list = list(map(int, input().split()))
sco_list.sort()
ans = 0
for i in range(food):
    cur_sco = (sco_list[i] * (pow(2, i, P) - pow(2, food-i-1, P))) % P
    ans += cur_sco
    ans = ans % P
print(ans)