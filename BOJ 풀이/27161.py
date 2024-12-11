import sys
input = sys.stdin.readline

cards = int(input())
cur_time = 0
acw_flag = False
for _ in range(cards):
    floor_flag = False
    card_type, card_time = map(str, input().rstrip().split())
    card_time = int(card_time)
    
    # step 1 / 지금 불러야 하는 것에 대해 판단.
    if acw_flag:
        cur_time -= 1
        if cur_time == 0:
            cur_time = 12
    else:
        cur_time += 1
        if cur_time == 13:
            cur_time = 1
            
    # 상위 룰 : 과부화의 법칙부터 flag
    if cur_time == card_time and card_type == 'HOURGLASS':
        pass
    elif cur_time == card_time:
        floor_flag = True
    elif card_type == 'HOURGLASS':
        if acw_flag: acw_flag = False
        else: acw_flag = True
    
    if floor_flag:
        print("%d %s"%(cur_time, 'YES'))
    else:
        print("%d %s"%(cur_time, "NO"))