# 7578
import sys
input = sys.stdin.readline

N = int(input())

# step 1. 세그트리를 위한 준비
# 확인 순서를 준비.
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_pos_dict = {}
for i in range(N):
    B_pos_dict[B[i]] = i + 1
    
seq_list = []
for a in A:
    seq_list.append(B_pos_dict[a])
    

# step 2. 세그트리 생성
# 원하는 것은 seq_list에서 i가 나오면 i번째에 + 1을 한다.
# 그리고 i 번째부터 N 까지의 합을 구해서 1을 빼자.

size = 1
while size <= N:
    size *= 2
    
tree = [0 for _ in range(2 * size)]
size -= 1

# 2-1. 트리 업데이트 수행 (그 위치에 줄을 만들기.)
def tree_update(idx):
    idx += size
    tree[idx] += 1
    idx //= 2
    
    while idx >= 1:
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
        idx //= 2
        

# 2-2. 트리 겹치는거 세기
def tree_interval_sum(i):
    left = i + size
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

result = 0
for s in seq_list:
    result += tree_interval_sum(s)
    tree_update(s)
print(result)