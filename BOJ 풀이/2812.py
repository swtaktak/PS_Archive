import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stack = []
num = list(input().rstrip())
for d in num:
    while stack and stack[-1] < d and K > 0:
        if K > 0:
            stack.pop()
            K -= 1
    stack.append(d)
while K > 0:
    stack.pop()
    K -= 1
print("".join(stack))