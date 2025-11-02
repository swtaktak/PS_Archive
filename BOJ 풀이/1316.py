import sys
input = sys.stdin.readline

def group_check(s):
    cur_l = ''
    hist = {}
    
    for c in s:
        if cur_l != c:
            if c in hist:
                return 0
            else:
                cur_l = c
                hist[c] = True
    return 1


N = int(input())
ans = 0

for _ in range(N):
    cur_word = str(input().rstrip())
    ans += group_check(cur_word)
    
print(ans)