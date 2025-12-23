# 2110
import sys
input = sys.stdin.readline

def get_gongyu(dist):
    cnt = 1                     # 첫 집에 하나 설치
    last = house_list[0]        # 마지막으로 설치한 집 위치

    for i in range(1, house):
        if house_list[i] - last >= dist:
            cnt += 1
            last = house_list[i]
    return cnt


house, gongyu = map(int, input().split())
house_list = []
for _ in range(house):
    house_list.append(int(input()))
    
house_list.sort()


start = 1
end = house_list[-1] - house_list[0]
ans = -1 # 딱뎀일때만 정답
while start <= end:
    mid = (start + end) // 2
    gongyu_need = get_gongyu(mid)
    
    if gongyu_need >= gongyu: # 필요한 공유기가 많거나 같아서 거리를 늘릴건데
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)