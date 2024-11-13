def get_piece(mid, lan_list):
    piece_cnt = 0
    for cur_len in lan_list:
        piece_cnt += (cur_len // mid)
    return piece_cnt

lan_cnt, lan_want = map(int, input().split())
lan_list = [0] * lan_cnt

for i in range(lan_cnt):
    length = int(input())
    lan_list[i] = length

left = 1
right = max(lan_list)
answer = 0

while left <= right:
    mid = (left + right) // 2
    piece_cnt = get_piece(mid, lan_list)
    
    # 조각이 더 적다면, 더 짧게 짤라야 한다.
    if piece_cnt < lan_want:
        right = mid - 1
    # 조각의 개수가 같다면, 더 살짝 길게 잘라보려 해야 한다.
    else:
        if mid > answer:
            answer = mid
        left = mid + 1
print(answer)