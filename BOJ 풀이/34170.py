import sys
input = sys.stdin.readline

# 개수가 K개인가..?

def solve(N, P, K):
    cur_cnt = 0
    cur_div = P
    while cur_div <= N:
        cur_cnt += (N // cur_div) - ((N-K) // cur_div) - (K // cur_div)
        cur_div *= P
    return cur_cnt


for i in range(50):
    cur_ans = solve(100, 7, i)
    print(i, cur_ans)

'''
T = int(input())
for _ in range(T):
    N, P, K = map(int, input().split())
    ans = solve(N, P, K)
    print(ans)
'''