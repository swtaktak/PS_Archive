import sys
input = sys.stdin.readline

tree, cost, value = map(int, input().split())
len_list = []

for _ in range(tree):
    len_list.append(int(input()))
    
max_len = max(len_list)
ans = 0

for cur_len in range(1, max_len + 1):
    cur_ans = 0
    for cur_tree in len_list:
        if cur_len <= cur_tree:
            cur_piece = (cur_tree // cur_len)
            if cur_tree % cur_len == 0:
                cur_cut = (cur_tree // cur_len - 1)
            else:
                cur_cut = (cur_tree // cur_len)
            if cur_piece * cur_len * value - cost * cur_cut > 0:
                cur_ans += cur_piece * cur_len * value - cost * cur_cut
    ans = max(cur_ans, ans)
print(ans)