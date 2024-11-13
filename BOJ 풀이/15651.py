N, M = map(int, input().split())
cur_list = []
def print_list(num_list):
    for i in range(M):
        if i < M-1:
            print(num_list[i], end = " ")
        else:
            print(num_list[i])
            
def dfs(level, cur_list):
    if level == M:
        print_list(cur_list)
        return
    else:
        for i in range(1, N+1):
            cur_list.append(i)
            dfs(level + 1, cur_list)
            # 가장 최근걸 없애야 한다. remove가 아니라 pop이어야 한다.!
            # 중복이 있단 말이야!
            cur_list.pop()
dfs(0, cur_list)