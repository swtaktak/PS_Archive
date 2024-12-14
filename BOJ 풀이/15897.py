# 배워 봅시다. Harmonic Lemma
# 더블카운팅을 적용하면, [N/1] + ....  + [N/N]을 계산하면 된다.
# 근데 10^9라서 계산이 무리다.
import sys
input = sys.stdin.readline

def div_cnt(N):
    ans = 0
    j = 0
    i = 1
    # Harmomic Lemma
    while i <= N:
        j = int(N / int(N/i)) 
        ans += (N // i) * (j - i + 1) 
        i = j + 1
    return ans

N = int(input())
answer = N + div_cnt(N-1)
print(answer)