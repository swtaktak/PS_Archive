import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    N = int(input())
    cur_list = list(map(str, input().rstrip().split()))
    
    if N == 1:
        print('NO')
    else:
        judge = True
        for i in range(N):
            if i == 0:
                if '-' in cur_list[i]:
                    judge = False
                    break
                else:
                    std = cur_list[i][-2:]
            else:
                if '-' in cur_list[i]:
                    judge = False
                    break
                elif std != cur_list[i][-2:]:
                    judge = False
                    break
        if not judge:
            print('NO')
        else:
            print('YES')