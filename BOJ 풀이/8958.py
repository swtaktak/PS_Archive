import sys
input = sys.stdin.readline

def get_score(s):
    combo = 0
    score = 0
    for c in s:
        if c == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    return score

T = int(input())
for _ in range(T):
    s = str(input().rstrip())
    print(get_score(s))