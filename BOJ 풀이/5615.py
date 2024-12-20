# 배워봅시다. 밀러 라빈 소수 판정법
# 페르마 소정리에 기반하여 나온 소수 판정법
# 실패 케이스를 모두 실패시키면 소수 아님! 선언
# 확률적인 방법이지만, 어지간한 수에서는 다 됨
import sys
input = sys.stdin.readline

def fast_pow(a, x, p):
    if x == 0:
        return 1
    elif x == 1:
        return a % p
    else: 
        half_val = fast_pow(a, x // 2, p)
        if x % 2 == 0:
            return (half_val * half_val) % p
        else:
            return (half_val * half_val * (a%p)) % p

def miller_rabin(n):
    prime_list = [2, 7, 61]
    if n == 1:
        return False
    elif n in prime_list:
        return True
    elif n % 2 == 0:
        return False
    else:
        d = n - 1
        pow2 = 0
        while d % 2 == 0:
            pow2 += 1
            d = d // 2
        # n과 pow2로 구분하였다. n은 홀수 파트. 
        # 체크할 수에 대하여
        
        for p in prime_list:
            pass_flag = False
            cur_r = fast_pow(p, d, n)
            # part 1. a^홀수파트 = 1 mod p
            if cur_r == 1:
                pass_flag = True
            # part 2. 2를 곱해가면서 -1 mod p
            else:
                for i in range(0, pow2):
                    if i != 0:
                        cur_r = (cur_r ** 2) % n
                    if cur_r == n-1:
                        pass_flag = True
                        break
            if not pass_flag:
                return False
    return True 

N = int(input())
# 2x + 1이 소수입니까?
answer = 0
for _ in range(N):
    cur_num = int(input())
    if miller_rabin(2 * cur_num + 1):
        answer += 1
print(answer)