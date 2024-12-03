import sys
input = sys.stdin.readline

friend, max_diff = map(int, input().split())
present_list = []
for _ in range(friend):
    present_list.append(list(map(int, input().split())))

# 가격, 만족도 순서, 가격을 오름차순으로 정렬한다.
present_list.sort(key = lambda x: (x[0], x[1]), reverse= False)
cur_happy = 0
max_happy = 0
start = 0
end = 0
while end < friend:
    cur_price_diff = present_list[end][0] - present_list[start][0]
    if cur_price_diff < max_diff:
        cur_happy += present_list[end][1]
        end += 1
    else:
        cur_happy -= present_list[start][1]
        start += 1
    max_happy = max(max_happy, cur_happy)
print(max_happy)
