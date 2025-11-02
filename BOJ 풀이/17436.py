# bitmasking + 포함 배제의 원리
# lcm 구해서 계산하기.
# 짝수개일 경우 빼고, 홀수개일 경우 더한다.
import sys
input = sys.stdin.readline

def get_bin(x):
    ans = ''
    one_cnt = 0
    while x > 0:
        ans += str(x % 2)
        if x % 2 == 1:
            one_cnt += 1
        x = x // 2
    ans = ans + ('0' * (N - len(ans)))
    return [ans, one_cnt]

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0
for cur_code in range(1, 2 ** N):
    code, one_cnt = get_bin(cur_code)
    lcm = 1
    cur_num_list = []
    
    for i in range(N):
        if code[i] == '1':
            lcm = lcm * num_list [i]
    if one_cnt % 2 == 1:
        ans += (M // lcm)
    else:
        ans -= (M // lcm)
print(ans)