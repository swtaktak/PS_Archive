N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
cur_list = []

def print_list(num_list):
    for i in range(M):
        if i < M-1:
            print(num_list[i], end = " ")
        else:
            print(num_list[i])
            
def dfs(start, level, cur_list):
    if level == M:
        print_list(cur_list)
        return
    else:
        # 동일한 깊이에서 같은 숫자를 또 안 쓰게 하기 / 해당 깊이에서 숫자가 안겹치는가.
        overlap_num = -1
        for i in range(start, N):
            if overlap_num != num_list[i]:
                cur_list.append(num_list[i])
                # 현 깊이에서, 중복 숫자 체크함. 다음 dfs에는 깊이가 달라짐.
                # dfs가 끝나면 현 깊이로 돌아오므로 중복 체크가 발생.
                overlap_num = num_list[i] 
                dfs(i, level+1, cur_list)
                cur_list.pop()
dfs(0, 0, cur_list)

