import sys
input = sys.stdin.readline
def dfs(level, cur_pos):
    if level == 6:
        for i in range(0, 6):
            print(pick_list[i], end = " ")
        print()
        return

    for i in range(cur_pos, len(cur_pool)):
        if not visited[i]:
            visited[i] = True
            pick_list.append(cur_pool[i])
            dfs(level + 1, i)
            visited[i] = False
            pick_list.pop()

while True:
    cur_list = list(map(int, input().split()))
    
    if cur_list[0] == 0:
        break
    else:
        cur_pool = cur_list[1:]
        pick_list = []
        visited = [False] * len(cur_pool)
        dfs(0, 0)
        print()
        