# 팰린드롬이 되기 위해서는
# 알파벳이 모두 달라야 한다.
# 하나의 알파벳 카드만 몽땅 넣거나.
# a, b 형태만 넣던가.
import sys
input = sys.stdin.readline
p = 1000000007
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
            return (half_val * half_val * (a%c)) % p

N = int(input())
s = str(input().rstrip())
alpha_dict = {}
for c in s:
    if c not in alpha_dict:
        alpha_dict[c] = 1
    else:
        alpha_dict[c] += 1

cnt_list = list(alpha_dict.values())
answer = 0
for c in cnt_list:
    if c >= 2:
        answer += (fast_pow(2, c, p) - (c + 1)) % p
for i in range(len(cnt_list)-1):
    for j in range(i+1, len(cnt_list)):
        answer += (cnt_list[i] * cnt_list[j]) % p

print(answer % p)