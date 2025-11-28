# 12904 A와 B
# 발상의 전환.
# S에서 T로 가는 거는 못본다.
# 근데 T에서 S로 갈 수 있다.

import sys
input = sys.stdin.readline
start = str(input().rstrip())
end = str(input().rstrip())

while len(end) > len(start):
    if end[-1] == 'A':
        end = end[:-1]
    else:
        end = end[:-1][::-1]

if start == end:
    print(1)
else:
    print(0)