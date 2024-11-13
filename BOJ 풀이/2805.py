
def bring_len(cut, trees):
    length = 0
    for t in trees:
        if t >= cut:
            length += (t - cut)
    return length

num_tree, goal_len = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
max_height = 0

while left <= right:
    mid = (left + right) // 2
    cur_get = bring_len(mid, trees)
    
    if cur_get < goal_len:
        # 자르는 기준점이 더 낮아야 한다.
        right = mid - 1
    
    else:
        if mid > max_height:
            max_height = mid
        
        left = mid + 1
print(max_height)