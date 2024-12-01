

import sys
import heapq
input = sys.stdin.readline

gem, bag = map(int, input().split())
gem_list = []
for _ in range(gem):
    w, v = map(int, input().split())
    gem_list.append([w, v])


bag_list = []
for _ in range(bag):
    bag_list.append(int(input()))

# 가방에 보석 하나밖에 못 넣음에 주의.
# 가벼운 가방부터, 담을 수 있는 가장 큰 것을 담아라.
# 가벼운 보석부터 정리.
gem_list.sort(key = lambda x: x[0], reverse = True)
bag_list.sort()
answer = 0
cand_gems = []
heapq.heapify(cand_gems)

for i in range(bag):
    cur_bag = bag_list[i]
    while True:
        if gem_list:
            cur_gem = gem_list[-1][0]
            if cur_gem <= cur_bag:
                heapq.heappush(cand_gems, -gem_list[-1][1])
                gem_list.pop()
            else:
                break
        else:
            break
    # 담을 가능성이 있는 보석들을 모두 담았다.
    # 가장 높은 거를 준다.
    if cand_gems:
        input_val = -heapq.heappop(cand_gems)
        answer += input_val    
print(answer)