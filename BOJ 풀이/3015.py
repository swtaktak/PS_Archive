import sys
input = sys.stdin.readline

N = int(input())
ans = 0
stack = []
num_list = []
for _ in range(N):
    num_list.append(int(input()))
    
for i in range(N):
    
    # 최초 항 처리
    if i == 0:
        stack.append([num_list[i], 1])
    else:
        cur_h = num_list[i]
        
        if stack:
            if cur_h == stack[-1][0]:
                ans += stack[-1][1]
                stack[-1][1] += 1
            else:
                while stack:
                    if stack[-1][0] > cur_h:
                        break
                    else:
                        ans += stack[-1][1]
                        stack.pop()
                if stack:
                    ans += 1
        stack.append([num_list[i], 1])
print(ans)