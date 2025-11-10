# 시작은 6시 6분, 그 이후 12분 간격으로 출발.
# 인원은 50명 정원 버스

import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    front_p = int(input())
    # 가희까지 세야 한다! 가희까지!
    total_p = front_p + 1
    
    if total_p % 50 == 0:
        bus_cnt = total_p // 50
    else:
        bus_cnt = total_p // 50 + 1
    total_time = (bus_cnt-1) * 12 + 6
    
    if total_time > 1080:
        print(-1)
    else:
        ans_time = total_time + 360
        h = str(ans_time // 60)
        m = str(ans_time % 60)
        
        if len(h) == 1:
            h = '0' + h
         
        if len(m) == 1:
            m = '0' + m
        
        answer = h + ':' + m
        print(answer)