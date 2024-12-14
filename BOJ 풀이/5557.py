import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

for i in range(0, N-1):
    new_dict = {}
    if i == 0:
        new_dict[num_list[i]] = 1
        cur_dict = new_dict.copy()
    else:
        cur_num = num_list[i]
        for c in cur_dict:
            if c + cur_num <= 20:
                if c + cur_num not in new_dict:
                    new_dict[c + cur_num] = cur_dict[c]
                else:
                    new_dict[c + cur_num] += cur_dict[c]
            if c - cur_num >= 0:
                if c - cur_num not in new_dict:
                    new_dict[c - cur_num] = cur_dict[c]
                else:
                    new_dict[c - cur_num] += cur_dict[c]
        cur_dict = new_dict.copy()

if num_list[-1] in cur_dict:
    print(cur_dict[num_list[-1]])
else:
    print(0)