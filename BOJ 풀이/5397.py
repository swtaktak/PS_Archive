import sys
T = int(input())

for _ in range(T):
    logs = str(input().rstrip())
    
    new_ans = ''
    cursor = 0
    for l in logs:
        # ABCD
        if l not in ['<', '>', '-']:
            if cursor == len(new_ans):
                new_ans += l
                cursor += 1
            else:
                new_ans = new_ans[:cursor] + l + new_ans[cursor:]
                cursor += 1
        elif l == '-':
            if len(new_ans) > 0:
                if cursor == 1:
                    new_ans = new_ans[1:]
                    cursor -= 1
                elif cursor == len(new_ans):
                    new_ans = new_ans[:-1]
                    cursor -= 1
                else:
                    new_ans = new_ans[:cursor-1] + new_ans[cursor:]
                    cursor -= 1
        elif l == "<":
            if cursor > 0:
                cursor -= 1
        elif l == ">":
            if cursor != len(new_ans):
                cursor += 1
    print(new_ans)