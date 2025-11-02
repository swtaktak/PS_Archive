import sys
input = sys.stdin.readline

word_list = {}
while True:
    w = str(input().rstrip())
    if len(w) == 0 or w == '/n':
        break
    else:
        word_list[w] = True
    

ans_list = []
for w in word_list:
    len_w = len(w)
    for i in range(len_w):
        left = w[:i]
        right = w[i:]
        if len(left) > 0 and len(right) > 0:
            if left in word_list and right in word_list:
                ans_list.append(w)
                break
ans_list.sort()
for a in ans_list:
    print(a)