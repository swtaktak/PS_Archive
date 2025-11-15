# bottomup 방식의 구현
# bottom up 방식의 구현의 장점
# 반복문 구조로, 재귀보다도 더 빠르다.
# 트리의 인덱스를 특정할 수 있어 좌우놀이 하지 않는다.
import sys
input = sys.stdin.readline

N, change_cnt, sum_cnt = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

# 밑에서부터 가기에, tree_size부터 구해야 한다.
size = 1
while size < N:
    size *= 2
tree = [0 for _ in range(2 * size)]
size -= 1

# 인덱스는 top-down과 동일함. 

# Bottom up에서는 별도의 초기화 과정이 없음
# 업데이트를 통해 초기화를 같이 진행함.
def tree_update(tree_idx, diff):
    # tree 위 사이즈 만큼 가고, 나머지는 사이즈 뒤로 부여...
    tree_idx += size
    while tree_idx >= 1: # 굳이 0번을 건드릴 이유는 없으므로.
        # 자식부터 타고 올라가 부모 루트까지 싹 다 값 연산 실시.
        # 상위 노드는 그냥 반갈.
        tree[tree_idx] += diff
        tree_idx //= 2

# 좌측과 우측만 주어진 상태로, 구간 계산을 한다.
# 시작 번호, 끝 번호는 역시 size 추가
def tree_interval_sum(left, right):
    left += size
    right += size
    ans = 0
    while left <= right:
        # 만날때 까지 계산한다.
        
        # left가 오른쪽에 있다면, 그냥 위로 올라가면 범위가 넘어간다.
        # 현재 위치를 더하고, "오른쪽"에서 상위 노드를 봐야 하기에 + 1한다.
        # 그리고 반갈하여 올라간다.
        if left % 2 == 1:
            ans += tree[left]
            left += 1
        left //= 2
        
        # right가 왼쪽에 있다면 그냥 위로 올라가면 범위가 넘어간다.
        # 현재 위치를 더하고, "왼쪽"에서 상위노드를 봐야 하기에 -1한다.
        # 그리고 반갈하여 올라간다,
        if right % 2 == 0:
            ans += tree[right]
            right -= 1
        right //= 2
    return ans


# 트리 초기화 과정
# size는 2의 거듭제곱 (예: 8)
# leaves: [size .. size+N-1]
for i in range(N):
    tree[size + 1 + i] = num_list[i]

# 이건 반대로, 루트까지 역순으로 가야 자식들을 올바르게 합치게 됨
for i in range(size, 0, -1):
    tree[i] = tree[2*i] + tree[2*i+1]


for _ in range(sum_cnt + change_cnt):
    query, b, c = map(int, input().split())
    if query == 1:
        cur_num = tree[b + size]
        diff = c - cur_num
        tree_update(b, diff)
    else:
        ans = tree_interval_sum(b, c)
        print(ans)