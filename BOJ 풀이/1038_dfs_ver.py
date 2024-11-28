import sys
input = sys.stdin.readline

def dfs(level):
    global answer_list
    if level == 10:
        cur_ans = ''
        for i in range(0, 10):
            if visited[i]:
                cur_ans += str((9-i))
        if len(cur_ans) > 0:
            answer_list.append(int(cur_ans))
        return
    for i in range(level, 10):
        visited[i] = True
        dfs(i + 1)
        visited[i] = False
        dfs(i + 1)

N = int(input())
if N >= 1023:
    print(-1)
else:
    visited = [False] * 10
    answer_list = []
    dfs(0)
    answer_list = sorted(list(set(answer_list)))
    print(answer_list[N])