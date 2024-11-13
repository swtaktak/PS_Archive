import sys
stack = []
num = int(input())
for _ in range(num):
    cur_order = sys.stdin.readline().rstrip()
    if 'push' in cur_order:
        a, cur_num = cur_order.split()
        stack.append(cur_num)
    elif 'pop' == cur_order:
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif 'size' == cur_order:
        print(len(stack))
    elif 'empty' == cur_order:
        if stack: print(0)
        else: print(1)
    elif 'top' == cur_order:
        if stack:
            print(stack[-1])
        else:
            print(-1)