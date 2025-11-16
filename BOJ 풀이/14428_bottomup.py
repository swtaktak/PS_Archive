import sys
input = sys.stdin.readline

# 크기가 가장 작은 값의 인덱스를 출력하는 세그트리?
# 근데 추적이 어려우므로, 아예 비교 값에 index를 넣어버리자.
N = int(input())
num_list = list(map(int, input().split()))
INF = 10 ** 9 + 1

size = 1
while size < N:
    size *= 2
tree = [[INF, -1] for _ in range(2 * size)]
size -= 1

# 최솟값 업데이트는, 말단은 그냥 잡고, 상단에서 직접 비교해서 오게.
# 부분 시간복잡도 : log N
def tree_update(tree_idx, cur_list):
    tree_idx += size
    tree[tree_idx] = cur_list
    tree_idx //= 2
    
    while tree_idx >= 1:
        tree[tree_idx] = min(tree[tree_idx * 2], tree[tree_idx * 2 + 1])
        tree_idx //= 2
        
def tree_interval_min(left, right):
    left += size
    right += size
    min_val = [INF, N + 1]
    
    up_cnt = 0
    while left <= right:
        if left % 2 == 1:
            if min_val > tree[left]:
                min_val = tree[left]
            left += 1
        left //= 2
        
        if right % 2 == 0:
            if min_val > tree[right]:
                min_val = tree[right]
            right -= 1
        right //= 2
        up_cnt += 1
    return min_val[1]

# 트리 초기화
for i in range(N):
    tree[size + 1 + i] = [num_list[i], i + 1]
for i in range(size, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

Q = int(input())
for _ in range(Q):
    query, b, c = map(int, input().split())
    if query == 1:
        tree_update(b, [c, b])
    elif query == 2:
        ans = tree_interval_min(b, c)
        print(ans)