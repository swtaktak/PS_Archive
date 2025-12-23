import sys
input = sys.stdin.readline

T = int(input())
for cur_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    ans_list = []
    
    for i in range(N):
        max_val = num_list.pop()
        r_price = max_val * 3 // 4
        ans_list.append(r_price)
        num_list.remove(r_price)
    ans_list.sort()
    print("Case #%d:" %(cur_case), end = " ")
    for a in ans_list:
        print(a, end = " ")
    print()