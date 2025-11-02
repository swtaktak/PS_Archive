import sys
input = sys.stdin.readline

list = [i for i in range(1, 21)] * 6
for i in range(0, 120, 8):
    cur_list = list[i:i+8]
    cur_list.sort()
    for c in cur_list:
        print(c, end = " ")
    print()