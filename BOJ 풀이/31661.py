# 31661
# 문자열 찾아서 숫자로 변경하기
# prefix가 같은 문자열이 없어서, 나오면 그만임

# 나중에 진법으로 쓸거임

import sys
input = sys.stdin.readline

N = int(input()) # 이게 진법 base가 될거임
str_list=list(map(str, input().strip().split()))
alpha_to_num = {}
# 진법 문자열을 우선 정리한다다.
for i in range(N):
    alpha_to_num[str_list[i]] = i

num_list = []
given_string = str(input().rstrip())
cur_check = ''

for c in given_string:
    cur_check += c
    if cur_check in alpha_to_num:
        num_list.append(alpha_to_num[cur_check])
        cur_check = ''
        
ans = 0
num_list = num_list[::-1]
for i in range(0, len(num_list)):
    ans += (num_list[i] * (N ** i))
print(ans)