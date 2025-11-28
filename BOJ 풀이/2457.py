import sys
input = sys.stdin.readline

flower_list = []
flower = int(input())
for _ in range(flower):
    bloom_m, bloom_d, wither_m, wither_d = map(int, input().split())
    # 날짜 리스트 핌~짐
    flower_list.append([bloom_m*100+bloom_d, wither_m*100+wither_d])

flower_list.sort()
count = 0
end_date = 301

while flower_list:
    # 11월 30일까지 꽃이 지지 않고 버텨야 한다. 커트라인은 12월 1일
    # 혹은 지금 피는 꽃이 늦어버림
    if end_date >= 1201 or flower_list[0][0] > end_date:
        break
    
    cur_end_date = -1
    
    for _ in range(len(flower_list)):
        # 현재 가장 먼저 필 꽃을 확인한다.
        cur_flower = flower_list[0]
        # 현재 가장 먼저 필 꽃이, 앞의 꽃이 지기 전에 핀다면
        if cur_flower[0] <= end_date:
            cur_end_date = max(cur_end_date, cur_flower[1])
            flower_list.remove(flower_list[0])
        else:
            break  
    end_date = cur_end_date
    count += 1

if end_date >= 1201:
    print(count)
else:
    print(0)