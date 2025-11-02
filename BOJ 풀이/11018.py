import sys
input = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP
gravity = 9.81

T = int(input())
for cur_case in range(1, T+1):
    print('Data Set %d:' %(cur_case))
    rocket_stage, rocket_mass = map(float, input().split())
    rocket_stage = int(rocket_stage)
    rocket_info = []
    total_mass = rocket_mass
    for _ in range(rocket_stage):
        cur_mass, cur_time, cur_power = map(float, input().split())
        total_mass += cur_mass
        rocket_info.append([cur_mass, cur_time, cur_power])
    cur_acc = 0
    cur_dist = 0
    cur_vec = 0
    
    for i in range(rocket_stage):
        cur_mass, cur_time, cur_power = rocket_info[i]
        cur_acc = cur_power / total_mass - gravity
        cur_dist += cur_vec * cur_time + (0.5 * cur_acc * (cur_time ** 2))
        cur_vec = cur_vec + cur_acc * cur_time
        total_mass = total_mass - cur_mass

    answer = Decimal(cur_dist)
    round_answer = answer.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(round_answer)
    print()