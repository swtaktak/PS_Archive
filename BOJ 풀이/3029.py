cur_time = list(map(int, input().split(":")))
throw_time = list(map(int, input().split(":")))

cur_time_sec = 3600 * cur_time[0] + 60 * cur_time[1] + cur_time[2]
throw_time_sec = 3600 * throw_time[0] + 60 * throw_time[1] + throw_time[2]

if cur_time_sec >= throw_time_sec:
    throw_time_sec += 86400
    
waiting_sec = throw_time_sec - cur_time_sec
wh = str(waiting_sec // 3600)
wm = str((waiting_sec % 3600) // 60)
ws = str(waiting_sec % 60)
if len(wh) == 1 : wh = '0' + wh
if len(wm) == 1 : wm = '0' + wm
if len(ws) == 1 : ws = '0' + ws
print(wh + ":" + wm + ":" + ws)