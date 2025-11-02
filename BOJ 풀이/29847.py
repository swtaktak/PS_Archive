import sys
input = sys.stdin.readline
ans_dict = {}

N = int(input())
for _ in range(N):
    s = str(input().rstrip())
    for c in s:
        if c != ' ':
            if c not in ans_dict:
                ans_dict[c] = 1
            else:
                ans_dict[c] += 1
for a in ans_dict:
    print("%c %d" %(a, ans_dict[a]))