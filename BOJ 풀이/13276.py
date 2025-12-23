import sys
input = sys.stdin.readline

S = input().rstrip()
pre = input().rstrip()
sux = input().rstrip()
pre_len = len(pre)
sux_len = len(sux)

pre_idx = []
sux_idx = []

for i in range(len(S) - pre_len + 1):
    if S[i:i+pre_len] == pre:
        pre_idx.append(i)

for i in range(len(S) - sux_len + 1):
    if S[i:i+sux_len] == sux:
        sux_idx.append(i)

ans_set = set()
cnt = 0

for p in pre_idx:
    prefix_end = p + pre_len - 1
    for s in sux_idx:
        if s < p:               
            continue
        suffix_end = s + sux_len - 1
        if suffix_end < prefix_end:
            continue

        cur_sub = S[p:suffix_end+1]
        if cur_sub not in ans_set:
            ans_set.add(cur_sub)
            cnt += 1

print(cnt)
