import sys
import heapq
input = sys.stdin.readline


# 고릴라 이름과, 고릴라 정보 가치가 heap으로 들어간다.
info_dict = {}
ans_val = 0
Q = int(input())
for _ in range(Q):
    cur_list = list(map(str, input().rstrip().split()))
    for i in range(len(cur_list)):
        if i != 1:
            cur_list[i] = int(cur_list[i])
    
    # 쿼리 1 : 고릴라 정보 가져옴
    if cur_list[0] == 1:
        gor_name = cur_list[1]
        # 초기화
        if gor_name not in info_dict:
            info_dict[gor_name] = []
        for i in range(3, len(cur_list)):
            cur_val = cur_list[i]
            heapq.heappush(info_dict[gor_name], -1 * cur_val)
    
    # 쿼리 2 : 고릴라에게 정보를 캠
    # 주의 사항 : 아직 이름이 없는 고릴라에게는 아무것도 얻지 못함
    if cur_list[0] == 2:
        gor_name = cur_list[1]
        if gor_name in info_dict:
            # 가지고 있는 정보와 필요 개수만큼 가져온다.
            pop_cnt = min(len(info_dict[gor_name]), cur_list[2])
            for _ in range(pop_cnt):
                cur_val = -1 * heapq.heappop(info_dict[gor_name])
                # print("I buy %d val to %s" % (cur_val, gor_name))
                ans_val += cur_val
print(ans_val)