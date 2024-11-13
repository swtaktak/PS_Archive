weight = int(input())
cur_5 = weight // 5
flag = False

while cur_5 >= 0:
    left_w = weight - cur_5 * 5
    if left_w % 3 == 0:
        flag = True
        print(cur_5 + left_w // 3)
        break
    else:
        cur_5 -= 1
if not flag:
    print(-1)