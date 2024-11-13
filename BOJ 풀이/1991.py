# mid, left, right
# preorder, inorder, postorder
import sys
input = sys.stdin.readline
n_nodes = int(input())

def preorder(root):
    print(root, end = "")
    cur_child_list = tree_info[root]
    if cur_child_list[0] != ".":
        preorder(cur_child_list[0])
    if cur_child_list[1] != ".":
        preorder(cur_child_list[1])

def inorder(root):
    cur_child_list = tree_info[root]
    if cur_child_list[0] != ".":
        inorder(cur_child_list[0])
    print(root, end = "")
    if cur_child_list[1] != ".":
        inorder(cur_child_list[1])
        
def postorder(root):
    cur_child_list = tree_info[root]
    if cur_child_list[0] != ".":
        postorder(cur_child_list[0])
    if cur_child_list[1] != ".":
        postorder(cur_child_list[1])
    print(root, end = "")

tree_info = {}
start_idx = -1
for i in range(n_nodes):
    root, left, right = map(str, input().rstrip().split())
    tree_info[root] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")