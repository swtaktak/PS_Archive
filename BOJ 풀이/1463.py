N = int(input())
num_list = [-1] * (N+1)
for i in range(1, N+1):
    if i == 1:
        num_list[i] = 0
    elif i <= 3:
        num_list[i] = 1
    else:
        cand_list = []
        cand_list.append(num_list[i-1])
        if i % 2 == 0: cand_list.append(num_list[i//2])
        if i % 3 == 0: cand_list.append(num_list[i//3])
        
        num_list[i] = min(cand_list) + 1
print(num_list[-1])