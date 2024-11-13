def find_num(num, num_list):
    start = 0
    end = len(num_list) - 1
    
    while start<=end:
        mid = (start + end) // 2
        
        if num_list[mid] < num:
            start = mid + 1
        
        elif num_list[mid] > num:
            end = mid - 1
        
        elif num_list[mid] == num:
            return 1
    return 0

list_size = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
check_cnt = int(input())
chk_list = list(map(int, input().split()))

for c in chk_list:
    print(find_num(c, num_list))