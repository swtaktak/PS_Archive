import sys
input = sys.stdin.readline
b_size, money, wage, keys = map(int, input().split())
key_card_list = []
# 1 : bank +,  2 : bank -,  3: fund  4 : go
for _ in range(keys):
    key_idx, key_value = map(int, input().split())
    key_card_list.append((key_idx, key_value))
map_info = ['S']
visited_dict = {}
for i in range(1, 4*b_size - 4):
    if i  == b_size - 1:
        map_info.append('nobody')
    elif i == 2 * (b_size - 1):
        map_info.append('fund')
    elif i == 3 * (b_size - 1):
        map_info.append('space')
    else:
        cur_pos = list(map(str, input().rstrip().split()))
        if cur_pos[0] == 'G':
            map_info.append('key')
        else:
            map_info.append('L' + '_' + str(cur_pos[1]))
            visited_dict[i] = False

# 초기화가 필요한 변수 목록
cur_pos = 0
is_nobody = False
nobody_cnt = 0
total_fund = 0
key_pos = 0
lose_flag = False

# 실제 게임 구현 구간.
dice_throw = int(input())
for _ in range(dice_throw):
    a, b = map(int, input().split())
    # 무인도 도중이라면
    if is_nobody:
        if a == b:
            is_nobody = False
            nobody_cnt = 0
        else:
            nobody_cnt += 1
            if nobody_cnt == 3:
                is_nobody = False
                nobody_cnt = 0
    # 무인도가 아닐 때의 진행
    else:
        cur_pos += (a + b)
        # 시작점을 밟거나 통과할 경우
        if cur_pos >= (4 * b_size - 4):
            money += wage * (cur_pos // (4 * b_size - 4))
            cur_pos %= (4 * b_size - 4)
        # 이벤트 처리
        if map_info[cur_pos] == 'nobody':
            is_nobody = True
        elif map_info[cur_pos] == 'fund':
            money += total_fund
            total_fund = 0
        elif map_info[cur_pos] == 'space':
            cur_pos = 0
            money += wage # 우주여행으로 급여 처리 필요!
        elif map_info[cur_pos] == 'key':
            idx, val = key_card_list[key_pos]
            if idx == 1:
                money += val
            elif idx == 2:
                money -= val
                if money < 0:
                    lose_flag = True
                    break
            elif idx == 3:
                money -= val
                total_fund += val
                if money < 0:
                    lose_flag = True
                    break
            else:
                cur_pos += val
                if cur_pos >= (4 * b_size - 4):
                    money += wage * (cur_pos // (4 * b_size - 4))
                    cur_pos %= (4 * b_size - 4)
                # 추가 이벤트 처리
                if map_info[cur_pos] == 'nobody':
                    is_nobody = True
                elif map_info[cur_pos] == 'fund':
                    money += total_fund
                    total_fund = 0
                elif map_info[cur_pos] == 'space':
                    cur_pos = 0
                    money += wage 
                elif map_info[cur_pos] != 'S':
                    land_price = int(map_info[cur_pos][2:])
                    if not visited_dict[cur_pos] and money >= land_price:
                        money -= land_price
                        visited_dict[cur_pos] = True
            key_pos = (key_pos + 1) % keys
        elif map_info[cur_pos] != 'S':
            land_price = int(map_info[cur_pos][2:])
            if not visited_dict[cur_pos] and money >= land_price:
                money -= land_price
                visited_dict[cur_pos] = True
for v in visited_dict:
    if not visited_dict[v]:
        lose_flag = True
        break
if lose_flag:
    print('LOSE')
else:
    print('WIN')