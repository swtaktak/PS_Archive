import sys
queue = []
N = int(input())

for _ in range(N):
    cur_order = sys.stdin.readline().rstrip()
    if "push" in cur_order:
        a, num = cur_order.split()
        queue.append(num)
    elif "pop" == cur_order:
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif "size" == cur_order:
        print(len(queue))
    elif "empty" == cur_order:
        if not queue: print(1)
        else: print(0)
    elif "front" == cur_order:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif "back" == cur_order:
        if not queue:
            print(-1)
        else:
            print(queue[-1])       