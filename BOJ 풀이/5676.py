# 양수, 0, 음수
# 세그트리 복습 문제
import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break  # EOF
    N, Q = map(int, line.split())
    num_list = list(map(int, input().split()))
    
    size = 1
    
    while size < N:
        size *= 2
        
    tree = [1 for _ in range(2 * size)]
    size -= 1
    
    def tree_update(tree_idx, val):
        tree_idx += size
        if val > 0:
            tree[tree_idx] = 1
        elif val < 0:
            tree[tree_idx] = -1
        else:
            tree[tree_idx] = 0
        tree_idx //= 2
        while tree_idx >= 1:
            tree[tree_idx] = tree[tree_idx * 2] * tree[tree_idx * 2 + 1]
            tree_idx //= 2
    
    def tree_interval_prod(left, right):
        left += size
        right += size
        ans = 1
        
        while left <= right:
            if left % 2 == 1:
                ans *= tree[left]
                left += 1
            left //= 2
            
            if right % 2 == 0:
                ans *= tree[right]
                right -= 1
            right //= 2
        return ans
    
    # 초기화
    for i in range(N):
        if num_list[i] > 0:
            tree[size + 1 + i] = 1
        elif num_list[i] < 0:
            tree[size + 1 + i] = -1
        else:
            tree[size + 1 + i] = 0
    for i in range(size, 0, -1):
        tree[i] = tree[2 * i] * tree[2 * i + 1]
    
    ans_list = []    
    for _ in range(Q):
        cur_list = input().split()
        order = cur_list[0]
        num1 = int(cur_list[1])
        num2 = int(cur_list[2])

        
        if order == 'C':
            tree_update(num1, num2)
        elif order == 'P':
            prod = tree_interval_prod(num1, num2)
            if prod == 1:
                ans_list.append('+')
            elif prod == -1:
                ans_list.append('-')
            else:
                ans_list.append('0')
        
    print("".join(ans_list))