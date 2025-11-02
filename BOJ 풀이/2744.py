import sys
input = sys.stdin.readline

s = str(input().rstrip())
answer = ''
for c in s:
    if c.isupper():
        answer += c.lower()
    else:
        answer += c.upper()
print(answer)