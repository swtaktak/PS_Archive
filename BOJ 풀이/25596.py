# 마트료시카 II
# 이번에는 없는 포함관계를 만들면 안된다.
import sys
input = sys.stdin.readline

total_box, sub_box, add_cut = map(int, input().split())

graph = [[] for _ in range(total_box + 1)]
for i in range(1, total_box + 1):
    cur_list = list(map(int, input().split()))
    if cur_list[0] > 0:
        for c in cur_list[1:]:
            graph[i].append(c)
            
cur_box_num = 1
new_box_num = total_box + 1
add_box_cnt = 0
fail_flag = False
while cur_box_num < len(graph):
    cur_box = graph[cur_box_num]
    if len(cur_box) > sub_box:
        add_box_cnt += 1
        if add_box_cnt > add_cut:
            fail_flag = True
            break
        graph.append([])
        
        while len(graph[cur_box_num]) > sub_box - 1:
            cur_elt = graph[cur_box_num].pop()
            graph[-1].append(cur_elt)
        graph[cur_box_num].append(new_box_num)
        new_box_num += 1
    cur_box_num += 1

if fail_flag:
    print(0)
else:
    print(1)
    print(add_box_cnt)

    for i in range(1, len(graph)):
        cur_line = graph[i]
        print(len(cur_line), end = " ")
        for c in cur_line:
            print(c, end = " ")
        print()