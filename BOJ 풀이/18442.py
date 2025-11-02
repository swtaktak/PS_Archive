import sys
input = sys.stdin.readline

def dfs(cur_pos, level):
    global min_len
    global ans_list
    if level == P:
        cur_len = 0
        for p in pos_list:
            if p not in cur_list:
                cur_min = 1e18
                for c in cur_list:
                    cur_dist = min(abs(c - p), L - abs(c - p))
                    cur_min = min(cur_min, cur_dist)
                cur_len += cur_min
        if cur_len < min_len:
            min_len = min(min_len, cur_len)
            ans_list = cur_list.copy()
        return
    for i in range(cur_pos, V):
        if not visited[i]:
            visited[i] = True
            cur_list.append(pos_list[i])
            dfs(i, level + 1)
            visited[i] = False
            cur_list.pop()


V, P, L = map(int, input().split())
pos_list = list(map(int, input().split()))
min_len = 1e18

visited = [False for _ in range(V)]
cur_list = []
ans_list = []
dfs(0, 0)
ans_list.sort()
print(min_len)
for a in ans_list:
    print(a, end = " ")