# 중위를 후위로 바꾸시오!
import sys
input = sys.stdin.readline

infix = str(input().rstrip())
postfix = ''
stack = []

for c in infix:
    if c.isalpha():
        postfix += c
    else:
        if c == '(':
            stack.append(c)
        elif c in ['+', '-']: # 우선순위가 가장 낮아서, 모두 다 빼낸다.
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(c)
        elif c in ['*', '/']: # 우선순위가 같은 것들은 다 빼낸다.
            while stack and stack[-1] in ['*', '/']:
                postfix += stack.pop()
            stack.append(c)
        elif c == ')': # 모든 연산자를 다 빼낸다.
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
while stack:
    postfix += stack.pop()
print(postfix)