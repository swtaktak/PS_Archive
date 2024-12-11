# a는 97...
import sys
input = sys.stdin.readline

def alpha_adic(N):
    ans = ''
    while N > 0:
        cur_r = N % 26
        ans += chr(97 + cur_r)
        N = N // 26
    return ans[::-1]

def alpha_to_num(s):
    cnt = 0
    ans = 0
    for c in s[::-1]:
        ans += (ord(c) - 97) * (26 ** cnt)
        cnt += 1
    return ans

typed = int(input())       
if typed == 1:
    a, b = map(int, input().split())
    answer = alpha_adic(a + b)
    answer = ('a' * (13-len(answer))) + answer
    print(answer)
elif typed == 2:
    s = str(input().rstrip())
    answer = alpha_to_num(s)
    print(answer)