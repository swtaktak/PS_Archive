import math
num = int(input())
t_size = list(map(int, input().split()))
t_group, p_group = map(int, input().split())

t_order = 0
for cur_t in t_size:
    t_order += math.ceil(cur_t / t_group)
p_gp_order = num // p_group
p_single_order = num % p_group

print(t_order)
print("%d %d" %(p_gp_order, p_single_order))