#bottom up  방식 구현 먼저
# 이번에는 update가 없다.

import sys
input = sys.stdin.readline

N, query = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

# step 1. 트리 크기 설정
size = 1
while size <= N:
    size *= 2
    
min_tree = [1000000001 for _ in range(2 * size)]
max_tree = [0 for _ in range(2 * size)]
size -= 1

# step 2. 최대/최소 알고리즘
def tree_interval_minmax(left, right):
    left += size
    right += size
    min_ans = 1000000001
    max_ans = 0
    
    while left <= right:
        if left % 2 == 1:
            min_ans = min(min_tree[left], min_ans)
            max_ans = max(max_tree[left], max_ans)
            left += 1
        left //= 2
        
        if right % 2 == 0:
            min_ans = min(min_tree[right], min_ans)
            max_ans = max(max_tree[right], max_ans)
            right -= 1
        right //= 2
    return [min_ans, max_ans]

# step 3. 트리의 초기화
for i in range(N):
    min_tree[size + 1 + i] = num_list[i]
    max_tree[size + 1 + i] = num_list[i]
    
for i in range(size, 0 , -1):
    min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
    max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])

for _ in range(query):
    left, right = map(int, input().split())
    min_ans, max_ans = tree_interval_minmax(left, right)
    print("%d %d" %(min_ans, max_ans))