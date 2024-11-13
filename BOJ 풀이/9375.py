import sys
sys = sys.stdin.readline

t_num = int(input())
for _ in range(t_num):
    num_case = int(input())
    clothes_dict = {}
    for _ in range(num_case):
        c_name, c_type = map(str, input().split())
        if c_type not in clothes_dict:
            clothes_dict[c_type] = 1
        else:
            clothes_dict[c_type] += 1
    
    val_list = clothes_dict.values()
    count = 1
    for v in val_list:
        count *= (v+1)
    print(count - 1)