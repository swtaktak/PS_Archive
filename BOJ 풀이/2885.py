import sys
input = sys.stdin.readline

def dec_to_revbin(N):
    ans = ''
    while N > 0:
        ans += str(N % 2)
        N = N // 2
    return ans

N = int(input())
min_buy = 1
while min_buy < N:
    min_buy *= 2

if N == min_buy:
    print("%d %d" %(min_buy, 0))
else:
    bin_rev = dec_to_revbin(N)
    ans_cnt = len(bin_rev)
    for i in range(ans_cnt):
        if bin_rev[i] == '1':
            break
        else:
            ans_cnt -= 1
    print("%d %d" %(min_buy, ans_cnt))