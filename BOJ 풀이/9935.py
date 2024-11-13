stack = []

o_string = str(input())
bomb = list(input())
bomb_len = len(bomb)

for cur_s in o_string:
    stack.append(cur_s)
    if len(stack) < bomb_len:
        pass
    elif cur_s == bomb[-1]:
        if stack[-bomb_len:] == bomb:
            for _ in range(bomb_len):
                stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))