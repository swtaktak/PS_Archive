import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

std, rel, money = map(int, input().split())
parent = [i for i in range(0, std + 1)]

money_list = [0] + list(map(int, input().split()))

if rel > 0:
    for _ in range(rel):
        left, right = map(int, input().split())
        union(left, right)
    
    p_dict = {}
    for i in range(1, std + 1):
        # 대상 접근시, parent는 직상위 밖에 못가져간다. find를 해야 최상위까지 올라간다.
        cur_parent = find(i)
        if cur_parent not in p_dict:
            p_dict[cur_parent] = money_list[i]
        else:
            if p_dict[cur_parent] > money_list[i]:
                p_dict[cur_parent] = money_list[i]
    
    # print(parent)
    need_money = 0
    for p in p_dict:
        need_money += p_dict[p]
        
    if need_money <= money:
        print(need_money)
    else:
        print('Oh no')

else:
    if sum(money_list) <= money:
        print(sum(money_list))
    else:
        print('Oh no')