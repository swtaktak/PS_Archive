import sys
input = sys.stdin.readline

def get_rep_score(s):
    lens = len(s)
    success_flag = False
    for cur_len in range(1, lens//2 + 1):
        if lens % cur_len == 0:
            cur_seg = s[:cur_len]
            cur_seg_flag = True
            for i in range(cur_len, lens, cur_len):
                now_seg = s[i:i+cur_len]
                if cur_seg != now_seg:
                    cur_seg_flag = False
                    break
            if cur_seg_flag:
                success_flag = True
                break
    if success_flag:
        return cur_len
    else:
        return lens

N = int(input())
virus = []
anti_virus = []

for _ in range(N):
    cur_s = str(input().rstrip())
    rep_s = get_rep_score(cur_s)
    virus.append(rep_s)
    
for _ in range(N):
    cur_s = str(input().rstrip())
    rep_s = get_rep_score(cur_s)
    anti_virus.append(rep_s)
    
virus.sort()
anti_virus.sort()

damage = 0
for i in range(N):
    damage += (virus[i] - anti_virus[i]) ** 2
print(damage)