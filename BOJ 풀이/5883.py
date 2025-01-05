import sys
input = sys.stdin.readline

N = int(input())
size_list = set()
line_list = []
for _ in range(N):
    cur_size = int(input())
    line_list.append(cur_size)
    size_list.add(cur_size)
    
size_list = list(size_list)
max_combo = 0
for pass_size in size_list:
    cur_combo = 1
    is_first = True
    for i in range(N):
        if is_first and line_list[i] != pass_size:
            is_first = False
            cur_size = line_list[i]
            cur_combo = 1
        elif line_list[i] != pass_size:
            if line_list[i] == cur_size:
                cur_combo += 1
            else:
                max_combo = max(max_combo, cur_combo)
                cur_size = line_list[i]
                cur_combo = 1
    max_combo = max(max_combo, cur_combo)
print(max_combo)