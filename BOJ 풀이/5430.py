from collections import deque
# 짝수번 뒤집으면 popleft, 홀수번 뒤집으면 pop

t_case = int(input())
for _ in range(t_case):
    cur_order = str(input())
    lens = int(input())
    arr = list(input().strip()[1:-1].split(","))
    q = deque(arr)
    
    rev_count = 0
    flag = True
    
    if lens == 0:
        q = []
        
    for c in cur_order:
        if c == "R":
            rev_count += 1
        elif c == "D":
            if not q:
                print("error")
                flag = False
                break
            else:
                if rev_count % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if flag:
        if rev_count % 2 == 0:
            print("[" + ",".join(map(str, list(q))) + "]")
        else:
            q.reverse()
            print("[" + ",".join(map(str, list(q))) + "]")