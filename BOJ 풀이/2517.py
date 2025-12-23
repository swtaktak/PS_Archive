import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    abil = int(input())
    num_list.append(abil)
query_list = num_list.copy()
num_list.sort()
abil_idx = {}
for i in range(N):
    abil_idx[num_list[i]] = i + 1 # idx 를 1-idx로 정렬
size = 1
while size <= N:
    size *= 2
tree = [0 for _ in range(2 * size)]
size -= 1

# tree update
def tree_update(idx):
    idx += size
    tree[idx] += 1
    idx //= 2
    
    while idx >= 1:
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
        idx //= 2

def tree_interval_sum(idx):
    left = idx + size
    right = N + size
    ans = 0
    
    while left <= right:
        if left % 2 == 1:
            ans += tree[left]
            left += 1
        left //= 2
        
        if right % 2 == 0:
            ans += tree[right]
            right -= 1
        right //= 2
    return ans

for n in query_list:
    cur_idx = abil_idx[n]
    print(tree_interval_sum(cur_idx) + 1)
    tree_update(cur_idx)