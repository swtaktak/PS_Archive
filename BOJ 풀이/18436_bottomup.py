import sys
input = sys.stdin.readline

# 짝, 홀 개수를 세는 세그트리?
# 홀수를 세자. 홀수를 세고, 짝수는 전체개수 - 홀수
# 홀수를 1, 짝수를 0으로 두고 합 세그트리 그대로~

N = int(input())
num_list = list(map(int, input().split()))

size = 1
while size < N:
    size *= 2
tree = [0 for _ in range(2 * size)]
size -= 1

def tree_update(tree_idx, cur_num):
    tree_idx += size
    tree[tree_idx] = cur_num % 2
    tree_idx //= 2
    
    while tree_idx >= 1:
        tree[tree_idx] = tree[tree_idx * 2] + tree[tree_idx * 2 + 1]
        tree_idx //= 2
        
def tree_interval_odd(left, right):
    left += size
    right += size
    cnt = 0
    
    while left <= right:
        if left % 2 == 1:
            cnt += tree[left]
            left += 1
        left //= 2
        
        if right % 2 == 0:
            cnt += tree[right]
            right -= 1
        right //= 2
    
    return cnt

for i in range(N):
    tree[size + 1 + i] = num_list[i] % 2
for i in range(size, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]

Q = int(input())
for _ in range(Q):
    query, left, right = map(int, input().split())
    if query == 1:
        tree_update(left, right)
    elif query == 2:
        ans = (right - left + 1) - tree_interval_odd(left, right)
        print(ans)
    elif query == 3:
        ans = tree_interval_odd(left, right)
        print(ans)