import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
col_list = list(map(int, input().split()))
row_list = list(map(int, input().split()))

col_parity_cum = []
row_parity_cum = []

for i in range(N):
    if i == 0:
        col_parity_cum.append(1)
        cur_parity = col_list[i] % 2
    else:
        if col_list[i] % 2 == cur_parity:
            col_parity_cum.append(col_parity_cum[-1])
        else:
            col_parity_cum.append(col_parity_cum[-1] + 1)
            cur_parity = col_list[i] % 2

for i in range(N):
    if i == 0:
        row_parity_cum.append(1)
        cur_parity = row_list[i] % 2
    else:
        if row_list[i] % 2 == cur_parity:
            row_parity_cum.append(row_parity_cum[-1])
        else:
            row_parity_cum.append(row_parity_cum[-1] + 1)
            cur_parity = row_list[i] % 2
            
for _ in range(Q):
    ca, ra, cb, rb = map(int, input().split())
    if col_parity_cum[ca-1] == col_parity_cum[cb-1] and row_parity_cum[ra-1] == row_parity_cum[rb-1]:
        print('YES')
    else:
        print('NO')