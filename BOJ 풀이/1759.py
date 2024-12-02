import sys
input = sys.stdin.readline

lens, chars = map(int, input().split())
char_list = list(map(str, input().rstrip().split()))
char_list.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
visited = [False] * chars

def dfs(cur_str, start):
    if len(cur_str) == lens:
        flag = False
        vowel_flag = False
        const_cnt = 0
        for c in cur_str:
            if c in vowel:
                vowel_flag = True
            else:
                const_cnt += 1
            if const_cnt >= 2 and vowel_flag:
                flag = True
                break
        if flag:
            print(cur_str)
        return
    for i in range(start, chars):
        if not visited[i]:
            visited[i] = True
            cur_str += char_list[i]
            dfs(cur_str, i+1)
            visited[i] = False
            cur_str = cur_str[:-1]
dfs('', 0)