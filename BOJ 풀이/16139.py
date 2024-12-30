import sys
input = sys.stdin.readline

s = str(input().rstrip())
alpha_dict = {}

for i in range(len(s)):
    cur_c = s[i]
    if cur_c not in alpha_dict:
        alpha_dict[cur_c] = [i]
    else:
        alpha_dict[cur_c].append(i)

Q = int(input())
for _ in range(Q):
    c, start, end = map(str, input().rstrip().split())
    start, end = int(start), int(end)
    
    if c not in alpha_dict:
        print(0)
    else:
        cur_count = 0
        idx_list = alpha_dict[c]
        
        for i in idx_list:
            if i >= start and i <= end:
                cur_count += 1
            elif i > end:
                break
        print(cur_count)