import sys
input = sys.stdin.readline

def bin_seed(seed):
    ans = ''
    while seed > 0:
        ans += str(seed % 2)
        seed = seed // 2
    ans = ans + '0' * (N - len(ans))
    return ans

N = int(input())
p_list = list(map(int, input().split()))
cnt = 0
for seed in range(0, 2 ** N):
    seed_code = bin_seed(seed)
    val = 0
    for i in range(len(seed_code)):
        if seed_code[i] == '1':
            val += (1 / p_list[i])
    if  0.99 <= val <= 1.01:
        cnt += 1
        
print(cnt)