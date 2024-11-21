import sys
input = sys.stdin.readline

crane_num = int(input())
crane_list = list(map(int, input().split()))
crane_list.sort(reverse = True)

box_num = int(input())
box_list = list(map(int, input().split()))
box_list.sort(reverse = True)

# 불가능 판단부터, 하나라도 못 실으면 탈락이니까. 그냥 이거로 됨.
if crane_list[0] < box_list[0]:
    print(-1)
else:
    time = 0
    # 실을 수 있다.
    while box_list:
        for cur_crane in crane_list:
            # 가망도 없다면 돌지 마라
            if box_list and cur_crane < box_list[-1]:
                continue
            else:
                for cur_box in box_list:
                    if cur_crane >= cur_box:
                        # 현재 실을 수 있는 가장 최고의 무게를 실자
                        box_list.remove(cur_box)
                        #  박스를 실으면, 박스를 더 안봐도 되게 함
                        break
        # 라운드 종료
        time += 1
    print(time)