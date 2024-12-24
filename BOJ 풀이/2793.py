import sys
input = sys.stdin.readline
# 구간별로 약수의 개수를 센다.
# 단 전 단계의 배수인데, 배수가 아닌 거를 센다.
# 그 다음에, 계산을 한다.
# 단, 1개일 경우에는 바로 그거지만 그 다음의 경우에는 1단계 더 가야 그거다.
# step 1 / lcm 리스트를 만든다.
# cutline 확보를 위해 어디까지 나눌 것인가?
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

cur_lcm = 1
cur_num = 2
lcm_dict = {}
while cur_lcm <= 10**17:
    cur_gcd = gcd(cur_num, cur_lcm)
    new_lcm = cur_lcm * cur_num // cur_gcd
    if len(lcm_dict) == 0:
        lcm_dict[cur_num] = new_lcm
    elif new_lcm != cur_lcm:
        lcm_dict[cur_num] = new_lcm
    cur_num += 1
    cur_lcm = new_lcm

chk_list = list(lcm_dict.keys())

# 이들의 변환 횟수를 세야 함?
base_dict = {}
for i in range(3, 43):
    for j in range(2, i + 1):
        if i % j != 0:
            base_dict[i] = j
            break

forty_two_dict = {}
for i in range(3, 43):
    step = 2
    cur_num = i
    while base_dict[cur_num] != 2:
        cur_num = base_dict[cur_num]
        step += 1
    forty_two_dict[i] = step

A, B = map(int, input().split())

# 최초 1단계가 몇 개인지만 보고 나머지는 직접 계산하자.
ans_dict = {}
for i in range(len(chk_list)):
    if i == 0:
        rev_cnt = B // 2 - (A-1) // 2
        cnt = (B - A + 1) - rev_cnt
        ans_dict[chk_list[i]] = cnt
    else:
        yes = lcm_dict[chk_list[i-1]]
        no = lcm_dict[chk_list[i]]
        yes_cnt = B // yes - (A-1) // yes
        no_cnt = B // no - (A-1) // no
        ans_dict[chk_list[i]] = yes_cnt - no_cnt

final_answer = 0
for a in ans_dict:
    if ans_dict[a] > 0:
        if a == 2:
            final_answer += (2 * ans_dict[a])
        else:
            final_answer += (forty_two_dict[a] + 1) * ans_dict[a]
print(final_answer)