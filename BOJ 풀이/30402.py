import sys
input = sys.stdin.readline
judge = False
for _ in range(15):
    cur_row = list(str(input().rstrip().split()))
    if not judge:
        if 'w' in cur_row:
            judge = True
            print('chunbae')
        if 'b' in cur_row:
            judge = True
            print('nabi')
        if 'g' in cur_row:
            judge = True
            print('yeongcheol')