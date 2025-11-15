# Top-Down 방식의 구현
# IDEA : 구간 합 트리를 생성한다. (세그먼트 트리)
# 부모 노드의 데이터의 범위를 반씩 나누어, 그 구간의 합을 저장한다.
# 이렇게 할 경우 변경되는 값은...트리로 추적할 수 있다.! 
import sys
input = sys.stdin.readline


# 세그먼트 트리는 3단계로 나누어 구현한다.
N, change_cnt, sum_cnt = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

# 트리의 길이는 포화 이진트리의 길이로 만든다.
# 그러나, 관습적(?) 으로  데이터의 개수에 4를 곱해서 미리 크기를 할당한다.
seg_tree = [0 for _ in range(4 * N)]

# 단계 1. tree_init
def tree_init(idx, left, right):
    # 구간에 데이터가 1개인 경우 (즉, 말단 노드)
    if left == right:
        # 현재의 인덱스 번호에 해당 값을 넣는다.
        seg_tree[idx] = num_list[left]
        return seg_tree[idx]
    else:
        # 구간에 데이터가 여러개일 경우 좌~중간, 중간+1~우 로 나눈다.
        # 좌측 자식은 2i, 우측 자식은 2i +  1
        # 그리고 이게 되기 위해, 루트 노드의 idx는 1이어야 한다.!!!!!!!
        mid = (left + right) // 2
        left_value = tree_init(2 * idx, left, mid)
        right_value = tree_init(2 * idx + 1, mid + 1, right)
        # 이 두 단계를 통과했음은, 자식 노드들이 완성되었다.
        # 부모노드는 자식 노드들의 합이므로
        seg_tree[idx] = left_value + right_value
        return seg_tree[idx]
    
# 단계 2. tree_update
# 바꿀 idx 값과 세그 idx 값을 잘 구분하자.
def tree_update(seg_idx, left, right, list_idx, change_val):
    # 최초 말단에서 바꿀 데이터 찾음
    if left == right == list_idx:
        seg_tree[seg_idx] = change_val
        return
    # 범위가 아닐 경우 바꾸면 안 된다.
    if list_idx < left or right < list_idx:
        return
    
    mid = (left + right) // 2
    # 왼쪽 자식 업데이트
    tree_update(seg_idx * 2, left, mid, list_idx, change_val)
    # 오른쪽 자식 업데이트
    tree_update(seg_idx * 2 + 1, mid + 1, right, list_idx, change_val)
    # 자식 업데이트 이후, 자식을 합친다.
    seg_tree[seg_idx] = seg_tree[2*seg_idx] + seg_tree[2*seg_idx + 1]
    
# 단계 3. tree_interval_sum
# 구간합을 구하는 단계
# start ~ end 까지의 값을 구한다.
# 이 때, left, right가 모두 포함되어 있다면 더해줘야 한다.
# 이걸 포함되는 최상단에서만 해주고 더 내려가면 안된다.
# 그 조각모음을 모두 해 줘야 한다.

def tree_interval_sum(start, end, seg_idx, left, right):
    # 구하고 싶은 구간(start ~ end)가 left, right 사이 벗어남 -> 더하면 X
    if end < left or right < start:
        return 0
    
    # 정확하게 포함이 되는 경우
    if start <= left and right <= end:
        return seg_tree[seg_idx]
    
    # 걸쳐 있어서 분할하는 경우
    mid = (left + right) // 2
    left_value = tree_interval_sum(start, end, seg_idx * 2, left, mid)
    right_value = tree_interval_sum(start, end, seg_idx * 2 + 1, mid + 1, right)
    return left_value + right_value
    

# 최초 트리 생성. 시작 idx 1에 다시 한번 주의 강조!
tree_init(1, 0, N-1)

for _ in range(change_cnt + sum_cnt):
    order, b, c = map(int, input().split())
    # change order : b-1번째 수를 c로 바꾼다.
    if order == 1:
        # idx 1부터 출발, 0~N-1번째 중 b-1번을 c로 바꿈
        tree_update(1, 0, N-1, b-1, c)
    else:
        # b-1번째 ~ c-1번째 합 구하기임
        ans = tree_interval_sum(b-1, c-1, 1, 0, N-1)
        print(ans)