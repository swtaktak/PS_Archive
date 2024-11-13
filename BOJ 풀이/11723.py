import sys
input = sys.stdin.readline

orders = int(input())
bits = [False] * 21

for _ in range(orders):
    cur_order = list(input().split())
    if "add" == cur_order[0]:
        num = int(cur_order[1])
        bits[num] = True
    elif "remove" == cur_order[0]:
        num = int(cur_order[1])
        bits[num] = False
    elif "check" == cur_order[0]:
        num = int(cur_order[1])
        if bits[num]:
            print(1)
        else:
            print(0)
    elif "toggle" == cur_order[0]:
        num = int(cur_order[1])
        if not bits[num]:
            bits[num] = True
        else:
            bits[num] = False
    elif "all" == cur_order[0]:
        bits = [True] * 21
    elif "empty" == cur_order[0]:
        bits = [False] * 21