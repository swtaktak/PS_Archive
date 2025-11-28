# 맛이 x : leaf index = size + (x - 1)
import sys
input = sys.stdin.readline


MAX_TASTE = 1000000
size = 1
while size < MAX_TASTE:
    size *= 2

tree = [0] * (2 * size)

def update(x, delta):
    idx = size + x - 1
    tree[idx] += delta
    idx //= 2
    
    while idx >= 1:
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx //= 2


def find_kth_candy(k):
    idx = 1
    while idx < size:
        # TOP k를 확인중이다. 왼쪽에서 순위가 다 찼으면 왼쪽에서 탐색, 부족하면 우측을 감
        left = idx * 2
        # 지금 순위가 더 위에 있어서 LEFT로 가야함
        if tree[left] >= k:
            idx = left
        else:
            # 순위가 더 밑에 있으면 LEFT만큼을 채우고, 잔여를 RIGHT에서 찾음.
            k = k - tree[left]
            idx = idx * 2 + 1
    # tree_idx를 leaf 자체로 변환
    taste = idx - size + 1
    return taste

# 초기화는 없다.
Q = int(input())
for _ in range(Q):
    order_list = list(map(int, input().split()))
    
    if order_list[0] == 2:
        update(order_list[1], order_list[2])
    elif order_list[0] == 1:
        # 사탕을 찾고 꺼내줘야 한다!
        cur_candy = find_kth_candy(order_list[1])
        update(cur_candy, -1)
        print(cur_candy)