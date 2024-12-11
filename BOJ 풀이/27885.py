import sys
input = sys.stdin.readline

def hour_to_sec(x):
    hour, min, sec = map(int, x.split(":"))
    return hour * 3600 + min * 60 + sec

# 쉽게 푸는 방법 : 비트마스킹
time_check = [True] * 86400
# 하나의 시간부터 40초까지의 범위가 차단기가 내려감
# 15~55초, 즉 41초가 아니라 빠져나가면 그즉시 차단기가 올라가 for 기준 40초.
up, down = map(int, input().split())
for _ in range(up):
    cur_up_time = str(input().rstrip())
    cur_up_sec = hour_to_sec(cur_up_time)
    for i in range(cur_up_sec, cur_up_sec + 40):
        time_check[i] = False

for _ in range(down):
    cur_down_time = str(input().rstrip())
    cur_down_sec = hour_to_sec(cur_down_time)
    for i in range(cur_down_sec, cur_down_sec + 40):
        time_check[i] = False

ans = 0
for i in range(86400):
    if time_check[i]:
        ans += 1
print(ans)