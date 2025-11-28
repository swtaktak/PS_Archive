import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dp_table = [[-1]*31 for _ in range(31)]

def dp(w, h):
    # 쉬운 가지치기.
    if w == 0:
        return 1
    # 이미 들린 상태를 반복하지 않도록
    if dp_table[w][h] != -1:
        return dp_table[w][h]
    
    ans = 0
    if w > 0:
        ans += dp(w-1, h+1)
    if h > 0:
        ans += dp(w, h-1)
        
    dp_table[w][h] = ans
    return ans

while True:
    N = int(input())
    if N == 0:
        break
    print(dp(N, 0))
