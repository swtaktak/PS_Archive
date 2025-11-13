import sys
input = sys.stdin.readline

N = int(input())
ma = []
mb = []

for _ in range(N):
    ma.append(list(map(int, input().split())))
for _ in range(N):
    mb.append(list(map(int, input().split())))
    
one_cnt = 0
for i in range(N):
    for j in range(N):
        # 행렬 i, j 성분에 대해 한다.
        judge = False
        for k in range(N):
            if ma[i][k] == 1 and mb[k][j] == 1:
                judge = True
                break
        if judge:
            one_cnt += 1
print(one_cnt)