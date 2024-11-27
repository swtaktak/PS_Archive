import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
goal = int(input())
wrong_button = int(input())
min_button = abs(goal-100)

if wrong_button == 0:
    press_cnt = len(str(goal))
    print(min(min_button, press_cnt))
    
else:
    wrong_list = list(map(int, input().split()))
    button_list = []
    for i in range(0, 10):
        if i not in wrong_list:
            button_list.append(str(i))

    def dfs(cur_ch, len):
        global min_button
        if len >= 7:
            return False
        elif len > 0:
            add_press = abs(int(cur_ch)-goal)
            total_press = add_press + len
            if total_press < min_button:
                min_button = total_press
        for cur_b in button_list:
            cur_ch += cur_b
            dfs(cur_ch, len+1)
            cur_ch = cur_ch[:-1]

    if not button_list:
        print(min_button)
    else:
        dfs("", 0) # 문자열과 길이
        print(min_button)