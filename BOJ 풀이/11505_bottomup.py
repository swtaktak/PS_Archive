# 반복연습하자.
# 11505 이번에는 곱셈 버전
import sys
input = sys.stdin.readline
P = 1000000007

N, change_cnt, prod_cnt = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

size = 1
while size < N:
    size *= 2
# 곱셈이어서 초기화 1
tree = [1 for _ in range(2 * size)]
size -= 1

def tree_update(tree_idx, new):
    tree_idx += size
    tree[tree_idx] = new % P
    # 다음 단계 위로 가서... 또 한다.
    tree_idx //= 2
    while tree_idx >= 1:
        # division zero 문제가 있어서 직접 재계산해야 한다.
        tree[tree_idx] = tree[tree_idx * 2] * tree[tree_idx * 2 + 1] % P
        tree_idx //= 2

def tree_interval_prod(left, right):
    left += size
    right += size
    ans = 1
    
    while left <= right:
        if left % 2 == 1:
            ans *= tree[left] % P
            left += 1
        left //= 2
        
        if right % 2 == 0:
            ans *= tree[right] % P
            right -= 1
        right //= 2
    return ans

# 초기화 단계
# 곱으로 변경, 나머지 미리 넣기
for i in range(N):
    tree[size + 1 + i] = num_list[i]

for i in range(size, 0, -1):
    tree[i] = (tree[2*i] * tree[2*i+1]) % P
    
for _ in range(prod_cnt + change_cnt):
    query, b, c = map(int, input().split())
    if query == 1:
        tree_update(b, c)
    else:
        ans = tree_interval_prod(b, c) % P
        print(ans)
    
