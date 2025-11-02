import sys
input = sys.stdin.readline
N, P = map(int, input().split())
cur_num = N
cnt = 1
visited = [-1 for _ in range(P)]
while True:
    cur_res = (N * cur_num) % P
    if visited[cur_res] != -1:
        answer = cnt - visited[cur_res]
        break
    else:
        visited[cur_res] = cnt
        cnt += 1
        cur_num = cur_res
print(answer)