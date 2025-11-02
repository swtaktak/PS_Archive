import sys
input = sys.stdin.readline

N = str(input().rstrip())

sum = 0
zero_flag = False
char_list = []
for c in N:
    sum += int(c)
    if c == '0':
        zero_flag = True
    char_list.append(c)
    
if zero_flag and sum % 3 == 0:
    char_list.sort(reverse = True)
    answer = ''
    for c in char_list:
        answer += c
    print(answer)
else:
    print(-1)