import sys
input = sys.stdin.readline

# 0  ~    n-1 node
# leaf 개수가 되는 트리 찾기
node, leaf = map(int, input().split())

# leaf 개수 만큼 빼 주면 됨

last_parent = node - leaf
for i in range(last_parent + 1, node):
    print("%d %d" %(last_parent, i))
    
for i in range(0, last_parent):
    print("%d %d" %(i, i + 1))