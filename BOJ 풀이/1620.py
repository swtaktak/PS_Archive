import sys
input = sys.stdin.readline

poke_num, q_num = map(int, input().split())
num_to_name_dict = {}
name_to_num_dict = {}

for i in range(1, poke_num + 1):
    cur_poke = str(input().rstrip())
    name_to_num_dict[cur_poke] = i
    num_to_name_dict[i] = cur_poke
    
for q in range(q_num):
    problem = str(input().rstrip())
    if str(problem).isdigit():
        print(num_to_name_dict[int(problem)])
    else:
        print(name_to_num_dict[str(problem)])
