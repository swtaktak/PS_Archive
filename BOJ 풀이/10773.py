import sys
input = sys.stdin.readline

stack = []
sum = 0

K = int(input())
for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
        sum += num
    elif stack:
        sum -= stack[-1]
        stack.pop()
print(sum)