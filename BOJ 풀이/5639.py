import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 전위는 부모, 왼쪽, 오른쪽 순서로 ... 
# 후위는 왼쪽 오른쪽 부모로 순서를 반대로...
preorder_list = []
while True:
    try:
        preorder_list.append(int(input()))
    except:
        break

def postorder(root_idx, end_idx):
    if root_idx > end_idx:
        return
    
    root_val = preorder_list[root_idx]
    right_idx = root_idx + 1
    
    while right_idx <= end_idx:
        if preorder_list[right_idx] > root_val:
            break
        else:
            right_idx += 1
    
    postorder(root_idx + 1, right_idx - 1)
    postorder(right_idx, end_idx)
    print(root_val)

postorder(0, len(preorder_list) - 1)