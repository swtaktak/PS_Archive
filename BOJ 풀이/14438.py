import sys
input = sys.stdin.readline

N = int(input())
num_list= list(map(int, input().split()))

size = 1
while size < N:
    size *= 2
tree = [0 for _ in range(2 * size)]
size -= 1

def tree_update(tree_idx, num):
    tree_idx += size
    tree[tree_idx] = num
    
    tree_idx //= 2
    while tree_idx >= 1:
        tree[tree_idx] = min(tree[tree_idx * 2], tree[tree_idx * 2 + 1])
        tree_idx //= 2
        
def tree_interval_min(left, right):
    left += size
    right += size
    ans = 1e9 + 1
    
    while left <= right:
        if left % 2 == 1:
            ans = min(tree[left], ans)
            left += 1
        left //= 2
        
        if right % 2 == 0:
            ans = min(tree[right], ans)
            right -= 1
        right //= 2
    return ans

for i in range(N):
    tree[size + 1 + i] = num_list[i]
for i in range(size, 0 , -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

Q = int(input())
for _ in range(Q):
    query, a, b = map(int, input().split())
    if query == 1:
        tree_update(a, b)
    else:
        ans = tree_interval_min(a, b)
        print(ans)