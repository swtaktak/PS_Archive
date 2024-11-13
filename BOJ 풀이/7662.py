import heapq
import sys
input = sys.stdin.readline

t_case = int(input())
for _ in range(t_case):
    min_heap = []
    max_heap = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    # 큐를 두개로 분할했지만, 실제로는 1개인 것처럼 운영해야 한다.
    
    num_counter = {}
    
    num_order = int(input())
    for _ in range(num_order):
        cur_ord_str = list(map(str, input().split()))
        cur_ord = cur_ord_str[0]
        cur_num = int(cur_ord_str[1])
        
        if cur_ord == "I":
            heapq.heappush(min_heap, cur_num)
            heapq.heappush(max_heap, -cur_num)
            if cur_num not in num_counter:
                num_counter[cur_num] = 1
            else:
                num_counter[cur_num] += 1
        else:
            # 최솟값 삭제
            if cur_num == -1:
                # step 1. 그게 실제로 존재하는 최솟값인가 이미 없어야 했던 애면 제거
                while min_heap and min_heap[0] not in num_counter:
                    heapq.heappop(min_heap)
                # step 2. 실제 최솟값을 제거한다.
                if min_heap:
                    cur_min = min_heap[0]
                    num_counter[cur_min] -= 1
                    if num_counter[cur_min] == 0:
                        del num_counter[cur_min]
                    heapq.heappop(min_heap)
            else:
                # step 1. 그게 실제로 존재하는 최댓값인가, 이미 없어야 했던 애면 제거
                while max_heap and -max_heap[0] not in num_counter:
                    heapq.heappop(max_heap)
                # step 2. 실제 최댓값을 제거한다. 음수에 주의
                if max_heap:
                    cur_max = -max_heap[0]
                    num_counter[cur_max] -= 1
                    if num_counter[cur_max] == 0:
                        del num_counter[cur_max]
                    heapq.heappop(max_heap)
    # 마지막으로 쓰레기 값 제거
    while min_heap and min_heap[0] not in num_counter:
        heapq.heappop(min_heap)
    while max_heap and -max_heap[0] not in num_counter:
        heapq.heappop(max_heap)
    # 최종 정답 출력, dict 확인
    empty_flag = True
    for cur_num in num_counter:
        if num_counter[cur_num] > 0:
            empty_flag = False
            break
        
    if empty_flag:
        print("EMPTY")
    else:
        print("%d %d" %(-max_heap[0], min_heap[0]))