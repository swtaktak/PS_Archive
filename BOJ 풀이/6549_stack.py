import sys
input = sys.stdin.readline

def solve(num_list):
    stack = []
    ans = 0
    
    num_list.append(0)
    
    for i in range(len(num_list)):
        # 새로운 막대의 높이가 stack의  top보다 짧다면, 그 때 pop하면서 넓이 계산
        while stack and num_list[stack[-1]] > num_list[i]:
            # 현재 높이 후보 idx를 준다.
            cur_height = num_list[stack.pop()]
            # stack에 아무것도 없을 경우, 0번부터 i번까지 이므로 i
            if not stack:
                width = i
            # stack에 뭐가 남아있을 경우 올바른 지점까지 계속 간다.
            else:
                width = i - stack[-1] - 1
            ans = max(ans, width * cur_height)
        stack.append(i)
    return ans


while True:
    num_list = list(map(int, input().split()))
    if num_list == [0]:
        break
    else:
        ans = solve(num_list[1:])
        print(ans)