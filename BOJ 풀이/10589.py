import sys
input = sys.stdin.readline

# idea : 짝수열, 짝수행만 몽땅 다 뒤집으면 된다.
rows, cols = map(int, input().split())

inv_cnt = rows // 2 + cols // 2
if inv_cnt == 0:
    print(0)
else:
    print(inv_cnt)
    if rows // 2 > 0:
        for i in range(2, rows + 1, 2):
            print("%d %d %d %d" %(i, 1, i, cols))
    if cols // 2 > 0:
        for j in range(2, cols + 1, 2):
            print("%d %d %d %d"%(1, j, rows, j))
