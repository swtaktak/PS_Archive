import sys
input = sys.stdin.readline

N = int(input())
ans = 0
stack = []

for _ in range(N):
    cur_h = int(input())
    if not stack:
        stack.append(cur_h)
    else:
        while stack and stack[-1] <= cur_h:
            stack.pop()
        stack.append(cur_h)
    ans += (len(stack) - 1)
print(ans)