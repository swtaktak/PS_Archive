import sys
input = sys.stdin.readline

T = int(input())
for cur_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_stack = []
    cost = 0
    
    for cur_n in num_list:
        if not num_stack:
            num_stack.append(cur_n)
        else:
            # 만일 대소가 뒤집힌다면..?
            # 이 때만 
            while num_stack and num_stack[-1] < cur_n:
                if len(num_stack) == 1:
                    num_stack.pop()
                    cost += cur_n
                else:
                    left = num_stack[-2]
                    right = cur_n
                    cost += min(left, right)
                    num_stack.pop()
            num_stack.append(cur_n)
    if len(num_stack) >= 2:
        cost += sum(num_stack[:-1])
    print("Case #%d: %d" %(cur_case, cost))