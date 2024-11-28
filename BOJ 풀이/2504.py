s = str(input())
stack = []
flag = True
for c in s:
    if c == '(':
        stack.append('(')
    elif c == '[':
        stack.append('[')
    elif c == ')':
        if not stack:
            break
        cur_number = 0
        while stack and stack[-1] != '(':
            if stack[-1] in ('[', ']', ')'):
                flag = False
                break
            elif stack[-1].isnumeric():
                cur_number += int(stack[-1])
                stack.pop()
        if stack and stack[-1] == '(':
            if cur_number == 0:
                stack.pop()
                stack.append('2')
            else:
                stack.pop()
                stack.append(str(cur_number * 2))
        elif not stack:
            flag = False
            break
    elif c == ']':
        if not stack:
            break
        cur_number = 0
        while stack and stack[-1] != '[':
            if stack[-1] in ('(' ,']', ')'):
                flag = False
                break
            elif stack[-1].isnumeric():
                cur_number += int(stack[-1])
                stack.pop()
        if stack and stack[-1] == '[':
            if cur_number == 0:
                stack.pop()
                stack.append('3')
            else:
                stack.pop()
                stack.append(str(cur_number * 3))
        elif not stack:
            flag = False
    if not flag:
        break
if not flag:
    print(0)
else:
    answer = 0
    for s in stack:
        if s in ('(', ')', '[', ']'):
            answer = 0
            break
        else:
            answer += int(s)
    print(answer)