N = int(input())
trophies = [0] * N

for i in range(N):
    h = int(input())
    trophies[i] = h
    
left_max = 0
left_see = 0
right_max = 0
right_see = 0

for i in range(N):
    cur_h = trophies[i]
    if cur_h > left_max:
        left_max = cur_h
        left_see += 1

for i in range(N-1, -1, -1):
    cur_h = trophies[i]
    if cur_h > right_max:
        right_max = cur_h
        right_see += 1
        
print(left_see)
print(right_see)