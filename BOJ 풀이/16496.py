import sys
input = sys.stdin.readline

def fill_num(n):
    cur_len = len(str(n))
    fill_cnt = fill_len//cur_len + 1
    answer = str(n) * fill_cnt
    return answer[:fill_len]

N = int(input())
num_list = sorted(list(map(int, input().split())))
fill_len = len(str(num_list[-1])) * 2  # 주의!  123, 1231 이런거 못가려냄!
# 최대 길이 만큼 숫자를 채워야 한다.
ans_list = []
for n in num_list:
    ans_list.append([str(n), fill_num(n)])

ans_list.sort(key = lambda x : (x[1], x[0]), reverse = True)
answer = ''
for a in ans_list:
    answer += a[0]
print(int(answer))