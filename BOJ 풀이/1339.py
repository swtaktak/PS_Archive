# idea : 아예 일반식으로 치환해서 계산하자
import sys
input = sys.stdin.readline

N = int(input())
alpha_val = {}
for i in range(N):
    cur_s = str(input().rstrip())
    for i in range(0, len(cur_s)):
        cur_c = cur_s[len(cur_s) - i - 1]
        if cur_c not in alpha_val:
            alpha_val[cur_c] = 10 ** i
        else:
            alpha_val[cur_c] += 10 ** i
val_list = sorted(list(alpha_val.values()), reverse=True)
start = 9
end = 10 - len(val_list)
answer = 0
for i in range(start, end-1, -1):
    answer += val_list[9-i] * i
print(answer)