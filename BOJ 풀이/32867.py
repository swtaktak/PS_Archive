import sys
input = sys.stdin.readline

touch, hand = map(int, input().split())
touch_list = list(map(int, input().split()))
cnt = 0

for i in range(touch):
    if i == 0:
        min_num = touch_list[i]
        max_num = touch_list[i]
    else:
        min_num = min(min_num, touch_list[i])
        max_num = max(max_num, touch_list[i])
        
        # 아오, 건반의 경우는 길이 차이 = 칸수 부족!  아오 ㅋㅋㅋㅋ
        if max_num - min_num >= hand:
            min_num = touch_list[i]
            max_num = touch_list[i]
            cnt += 1
print(cnt)