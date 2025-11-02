# 간단한 구현문제
import sys
input = sys.stdin.readline
press_num = list(map(int, input().split()))
ans = ''

num_dict = {'a': 2, 'b': 22, 'c': 222,
            'd': 3, 'e': 33, 'f': 333,
            'g': 4, 'h': 44, 'i': 444,
            'j': 5, 'k': 55, 'l': 555,
            'm': 6, 'n': 66, 'o': 666,
            'p': 7, 'q': 77, 'r': 777, 's': 7777,
            't': 8, 'u': 88, 'v': 888,
            'w': 9, 'x': 99, 'y': 999, 'z': 9999}

prev_num = -1

s = str(input().rstrip())

for c in s:
    cur_press = num_dict[c]
    if prev_num == cur_press % 10:
        ans += '#'
    ans += str(cur_press)
    prev_num = cur_press % 10

final_ans = ''
for a in ans:
    if a == '#':
        final_ans += a
    else:
        idx = press_num.index(int(a))
        final_ans += str(idx + 1)
print(final_ans)