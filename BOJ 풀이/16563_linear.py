import sys
input = sys.stdin.readline

# 어려운 소인수 분해 풀이 2 - 선형 체
MAX = 5000001
sieve = [0] * MAX
prime_list = []

for i in range(2, MAX):
    if sieve[i] == 0:
        prime_list.append(i)
        sieve[i] = i
    
    for p in prime_list:
        if i * p >= MAX:
            break
        
        sieve[i * p] = p
        if i % p == 0:
            break
        
N = int(input())
num_list = list(map(int, input().split()))
for n in num_list:
    cur_num = n
    while cur_num > 1:
        cur_div = sieve[cur_num]
        print(cur_div, end = " ")
        cur_num = cur_num // cur_div
    print("")