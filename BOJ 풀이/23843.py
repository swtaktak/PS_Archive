import sys
input = sys.stdin.readline

machine, charge = map(int, input().split())
m_list = list(map(int, input().split()))
m_list.sort(reverse = True)

answer = 0
stack = []
for m in m_list:
    # 사이클의 최초 시점
    if not stack:
        stack.append(m)
        cur_max = m
        answer += m
    # 충전기가 남았을 때, 최초보다 시간이 적냐 안적냐
    elif len(stack) < charge:
        if stack[-1] + m > cur_max:
            stack.append(m)
        else:
            stack[-1] += m
    else:
        if stack[-1] + m > cur_max:
            stack = []
            stack.append(m)
            cur_max = m
            answer += m
        else:
            stack[-1] += m
print(answer)