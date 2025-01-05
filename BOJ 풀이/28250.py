import sys
input = sys.stdin.readline

cnt_dict = {0:0, 1:0, 2:0}
# idea : 더블 카운팅.  어차피 2개씩 쌍을 보는 것이므로 세는 법을 바꾼다.
N = int(input())
num_list = list(map(int, input().split()))
for n in num_list:
    if n == 0:
        cnt_dict[0] += 1
    elif n == 1:
        cnt_dict[1] += 1
    else:
        cnt_dict[2] += 1
        
ans = 0
# 0과 0의 쌍은 1,  나머지 쌍은 0이므로 합이 아니다.
if cnt_dict[0] >= 2:
    ans += ((cnt_dict[0] * (cnt_dict[0]-1)) // 2)
# 0과 1의 쌍은 2
ans += 2 * (cnt_dict[0] * cnt_dict[1])
# 0과 2의 쌍은 1
ans += (cnt_dict[0] * cnt_dict[2])
print(ans)