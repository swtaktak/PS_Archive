# 유니온 파인드 문제
# 그래프의 성질, / 이미 분리된 집합 내부끼리 연결 시키려고 하면,
# 사이클이 확정적으로 생김을 활용한다.
# 즉, 새로운 멤버가 안들어 오면. 확정!
vertex, max_turn = map(int, input().split())
parent_list = [i for i in range(vertex)]
answer = 0

def find_top_parent(x):
    while x != parent_list[x]:
        x = parent_list[x]
    return x

def union_parent(x, y):
    x = find_top_parent(x)
    y = find_top_parent(y)
    
    if x > y:
        parent_list[x] = y
        return False
    elif x < y:
        parent_list[y] = x
        return False
    else:
        return True

for i in range(1, max_turn + 1):
    a, b= map(int, input().split())   
    if union_parent(a, b):
        print(i)
        break
    elif i == max_turn:
        print(0)