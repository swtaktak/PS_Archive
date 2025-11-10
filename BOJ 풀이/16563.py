import sys
input = sys.stdin.readline

# 어려운 소인수 분해 풀이 1 - 에라토스테네스의 체
# 선형 체라는 방법도 있다는데, 일단 이거부터.
# 수가 많아야 500만까지다. 500만의 0.5제곱 까지의 수만 봐도 된다.
# Python으로는 시초가 난다. 더 좋은 방법이 없을까?
MAX = 5000000
cutline = int(MAX ** 0.5) + 1
prime_check = [True for _ in range(cutline+ 1)]
for i in range(2, int(cutline ** 0.5) + 1):
    if prime_check[i]:
        for j in range(i*i, cutline+1, i):
            prime_check[j] = False
prime_list = [p for p in range(2, cutline + 1) if prime_check[p]]
N = int(input())
num_list = list(map(int, input().split()))

for n in num_list:
    cur_num = n
    for p in prime_list:
        while cur_num % p == 0:
            print(p, end = " ")
            cur_num = cur_num // p
    if cur_num > 1:
        print(cur_num, end = " ")
    print("")