import sys
def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

num = int(input())
if num == 0:
    print(0)
else:
    lv_list = []
    for i in range(num):
        lv_list.append(int(sys.stdin.readline().rstrip()))
        
    lv_list.sort()
    cut_line = roundUp(num * 0.15)
    avg = roundUp(sum(lv_list[cut_line:num-cut_line])/(num - 2 * cut_line))
    print(avg)