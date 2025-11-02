import sys
input = sys.stdin.readline

T = int(input())
for t_case in range(1, T+1):
    N = int(input())
    check_list = []
    for _ in range(N):
        cur_name = str(input().rstrip())
        check_list.append(cur_name)
    M = int(input())
    name_dict = {}
    for _ in range(M):
        cur_line = list(map(str, input().rstrip().split(" ")))
        for c in cur_line:
            if c not in name_dict:
                name_dict[c] = True
    print('Test set %d:' %(t_case))
    for c in check_list:
        if c in name_dict:
            print('%s is present' %(c))
        else:
            print('%s is absent' %(c))
    print()