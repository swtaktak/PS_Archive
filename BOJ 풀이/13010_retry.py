import sys
from collections import defaultdict
input = sys.stdin.readline

def gcd(a, b):
    if b > 0:
        a, b = b, a % b
    return a

def get_fact(n):
    N_divs = defaultdict(int)
    if n > 1:
        for i in range(2, int(n ** 0.5) + 2):
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    N_divs[i] += 1
        if n > 1:
            N_divs[n] += 1
    return N_divs

N = int(input())
answer = -1
fact_n = get_fact(N)
# 몇 제곱수가 최대인가? 이진법이 아니라 쉽게 계산하자.
fact_cnt_list = list(fact_n.values())
if len(fact_cnt_list) == 1:
    fact_gcd = fact_cnt_list[0]
else:
    for i in range(1, len(fact_cnt_list)):
        if i == 1:
            fact_gcd = gcd(fact_cnt_list[0], fact_cnt_list[1])
        else:
            fact_gcd = gcd(fact_cnt_list[i], fact_gcd)

answer = -1
for cur_pow in range(2, fact_gcd + 1):
    if fact_gcd % cur_pow == 0:
        # 현재 지수에 해당하는 밑 숫자를 구하고 그 숫자의 약수의 개수가, cur_pow와 동일한가?
        cur_num = 1
        div_cnt = 1
        for cur_f in fact_n:
            cur_num *= (cur_f ** (fact_n[cur_f] // cur_pow))
            div_cnt *= (fact_n[cur_f] // cur_pow + 1)
        if cur_pow == div_cnt:
            answer = cur_num
            break
print(answer)