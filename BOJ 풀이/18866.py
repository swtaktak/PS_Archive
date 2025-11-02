#  젊은 날의 생이여...
import sys
input = sys.stdin.readline

happy_list = [-1e9] + []
sad_list = [-1e9] + []

D = int(input())
for _ in range(D):
    happy, sad = map(int, input().split())
    happy_list.append(happy)
    sad_list.append(sad)
    
cum_min_happy = [-1 for _ in range(D + 1)]
cum_max_happy = [-1 for _ in range(D + 1)]
cum_min_sad = [-1 for _ in range(D + 1)]
cum_max_sad = [-1 for _ in range(D + 1)]

min_happy = 1e9
max_happy = -1
min_sad = 1e9
max_sad = -1
# 정방향 : 젊은 날
for i in range(1, D+1):
    if happy_list[i] != 0 and happy_list[i] < min_happy:
        min_happy = happy_list[i]
    cum_min_happy[i] = min_happy
    
    if sad_list[i] != 0 and sad_list[i] > max_sad:
        max_sad = sad_list[i]
    cum_max_sad[i] = max_sad
    
# 역방향 : 늙은 날
for i in range(D, 0, -1):
    if happy_list[i] != 0 and happy_list[i] > max_happy:
        max_happy = happy_list[i]
    cum_max_happy[i] = max_happy
    
    if sad_list[i] != 0 and sad_list[i] < min_sad:
        min_sad = sad_list[i]
    cum_min_sad[i] = min_sad

final_ans = -1
for ans in range(D-1, 0, -1):
    if cum_min_happy[ans] >= cum_max_happy[ans + 1]  and cum_max_sad[ans] <= cum_min_sad[ans + 1]:
        final_ans = ans
        break
    
print(final_ans)