import sys
input = sys.stdin.readline

x_dict = {}
y_dict = {}
cnt_sum = 0
N = int(input())
for _ in range(N):
    x, y, cnt = map(int, input().split())
    
    if x not in x_dict:
        x_dict[x] = cnt
    else:
        x_dict[x] += cnt
        
    if y not in y_dict:
        y_dict[y] = cnt
    else:
        y_dict[y] += cnt
        
    cnt_sum += cnt

x_list = []
y_list = []
for x in x_dict:
    x_list.append([x, x_dict[x]])
for y in y_dict:
    y_list.append([y, y_dict[y]])

x_list.sort(key = lambda x: x[0])
y_list.sort(key = lambda y: y[0])


if cnt_sum % 2 == 0:
    cutline = cnt_sum // 2

    x_cnt = 0
    for cur_x in x_list:
        cx, ccnt = cur_x[0], cur_x[1]
        x_cnt += ccnt
        if x_cnt >= cutline:
            x_answer = cx
            break

    y_cnt = 0
    for cur_y in y_list:
        cy, ccnt = cur_y[0], cur_y[1]
        y_cnt += ccnt
        if y_cnt >= cutline:
            y_answer = cy
            break
# 짝수인 경우, 어디가 더 유리? 그걸 모르므로 계산해야 한다.
else:
    cutline1 = cnt_sum // 2
    cutline2 = cnt_sum // 2 + 1
    
    x_cnt = 0
    for cur_x in x_list:
        cx, ccnt = cur_x[0], cur_x[1]
        x_cnt += ccnt
        if x_cnt >= cutline1:
            x_answer1 = cx
            break

    y_cnt = 0
    for cur_y in y_list:
        cy, ccnt = cur_y[0], cur_y[1]
        y_cnt += ccnt
        if y_cnt >= cutline1:
            y_answer1 = cy
            break

    x_cnt = 0
    for cur_x in x_list:
        cx, ccnt = cur_x[0], cur_x[1]
        x_cnt += ccnt
        if x_cnt >= cutline2:
            x_answer2 = cx
            break

    y_cnt = 0
    for cur_y in y_list:
        cy, ccnt = cur_y[0], cur_y[1]
        y_cnt += ccnt
        if y_cnt >= cutline2:
            y_answer2 = cy
            break
    
    # x_answer1과 x_answer2 중 어디가 더 유리
    x1_val = 0
    x2_val = 0
    
    for x in x_dict:
        x1_val += abs(x - x_answer1) * x_dict[x]
        x2_val += abs(x - x_answer2) * x_dict[x]
    if x1_val <= x2_val:
        x_answer = x_answer1
    else:
        x_answer = x_answer2
        
    # y_answer1과 y_answer2 중 어디가 더 유리
    y1_val = 0
    y2_val = 0
    
    for y in y_dict:
        y1_val += abs(y - y_answer1) * y_dict[y]
        y2_val += abs(y - y_answer2) * y_dict[y]
    if y1_val <= y2_val:
        y_answer = y_answer1
    else:
        y_answer = y_answer2
print("%d %d"%(x_answer, y_answer))