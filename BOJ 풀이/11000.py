import sys
import heapq

input = sys.stdin.readline

num_class = int(input())
timetable = []
for _ in range(num_class):
    start, end = map(int, input().split())
    timetable.append([start, end])
timetable.sort(key = lambda x: (x[0], x[1]))

end_time = []
heapq.heapify(end_time)

for i in range(num_class):
    cur_start, cur_end = timetable[i][0], timetable[i][1]
    if i == 0:
        heapq.heappush(end_time, cur_end)
    else:
        # 가장 빨리 끝나는 것과 비교. 우리가 더 일찍 시작하면 
        if cur_start < end_time[0]:
            heapq.heappush(end_time, cur_end)
        # 우리가 더 늦게 시작하면, 거기에 들어가 이어 하면 되니까 시간을 교체하면 된다.
        else:
            heapq.heappop(end_time)
            heapq.heappush(end_time, cur_end)
print(len(end_time))

