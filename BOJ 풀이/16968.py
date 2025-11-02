import sys
input = sys.stdin.readline

s = str(input().rstrip())
prev = 'x'
ans = 1
for c in s:
    if c == 'd' and prev != 'd':
        ans *= 10
    elif c == 'd' and prev == 'd':
        ans *= 9
    elif c == 'c' and prev != 'c':
        ans *= 26
    elif c == 'c' and prev == 'c':
        ans *= 25
    prev = c
print(ans)