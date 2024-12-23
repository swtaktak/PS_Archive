# 유니온 파인드 복습하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_top_parent(x):
    if x != parent_list[x]:
        parent_list[x] = find_top_parent(parent_list[x])
    return parent_list[x]

def union_parent_with_cnt(a, b):
    a = find_top_parent(a)
    b = find_top_parent(b)
    # 같지 않을 때만 이를 시도해야 함
    if a > b:
        parent_list[a] = b
        cnt_list[b] += cnt_list[a]
        cnt_list[a] = 0
    elif a < b:
        parent_list[b] = a
        cnt_list[a] += cnt_list[b]
        cnt_list[b] = 0
    

order = int(input())
parent_list = [x for x in range(10**6 + 1)]
cnt_list = [1 for _ in range(10**6 + 1)]
for _ in range(order):
    order_list = list(map(str, input().rstrip().split()))
    if order_list[0] == 'I':
        left, right = int(order_list[1]), int(order_list[2])
        union_parent_with_cnt(left, right)
    elif order_list[0] == 'Q':
        top_parent = find_top_parent(int(order_list[1]))
        print(cnt_list[top_parent])