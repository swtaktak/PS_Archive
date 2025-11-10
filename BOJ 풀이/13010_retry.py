import sys
input = sys.stdin.readline
# 가능한 x는 사실상 10**9 까지다. 정확하게는 root N
MAX = 10**9 + 1 # 안전하게
prime_num = []
prime_list = [True for _ in range(int(MAX ** 0.5) + 1)]
for i in range(2, len(prime_list)):
    if prime_list[i]:
        prime_num.append(i)
        for j in range(i*i, len(prime_list), i):
            prime_list[j] = False

def get_dn(n):
    if n == 1:
        return 1
    else:
        div_cnt = []
        for p in prime_num:
            cur_cnt = 0
            while n % p == 0:
                cur_cnt += 1
                n = n // p
            if cur_cnt > 0:
                div_cnt.append(cur_cnt)
        if n > 1:
            div_cnt.append(1)
        cnt = 1
        for d in div_cnt:
            cnt *= (d+1)
        return cnt
    
# 추가로....
# 약수의 개수가 많아야 60개임 61개부터는 무조건 실패임.
# 그 이유는 2 ** 60 > 10 ** 18 이어서.
N = int(input())
answer = MAX

if N == 1:
    print(1)
else:
    # 2제곱부터 59제곱까지만 하면 됨
    for cur_power in range(59, 1, -1):
        lower = 2
        upper = int(N ** (1/cur_power)) + 1
        
        while lower <= upper:
            mid = (lower + upper) // 2
            cur_val = mid ** cur_power
            if cur_val < N:
                lower = mid + 1
            else:
                if cur_val == N:
                    if get_dn(mid) == cur_power:
                        answer = mid
                upper = mid - 1
        if answer != MAX:
            break
        
if answer != MAX:
    print(answer)
else:
    print(-1)