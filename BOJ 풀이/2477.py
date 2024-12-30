# 긴거 두개 돌고... 나머지 4개 중 가운데 2개를 빼는 방식?
import sys
input = sys.stdin.readline

chamwae = int(input())
farm = []
way_dict = {1:0, 2:0, 3:0, 4:0}
for i in range(6):
    way, len = map(int, input().split())
    farm.append([way, len])
    way_dict[way] += 1
        
# 큰 쪽은 한번만 돈다.
long_way = []
for w in way_dict:
    if way_dict[w] == 1:
        long_way.append(w)

long_list = []
short_list = []
for i in range(6):
    if farm[i][0] in long_way:
        long_list.append(farm[i][1])
        start_idx = i

new_farm = farm * 2
for i in range(start_idx + 1, 12):
    if new_farm[i][0] in long_way:
        pass
    else:
        short_list.append(new_farm[i+1][1])
        short_list.append(new_farm[i+2][1])
        break
area = long_list[0] * long_list[1] - short_list[0] * short_list[1]
print(area * chamwae)

