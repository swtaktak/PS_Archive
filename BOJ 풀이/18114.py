import sys
input = sys.stdin.readline

def binary_search(target):
    start = 0
    end = stuff - 1
    
    while start <= end:
        mid = (start + end) // 2
        if thing_list[mid] == target:
            return True
        elif thing_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

stuff, weight = map(int, input().split())
thing_list = list(map(int, input().split()))
thing_list.sort()

flag = False
# 물건이 1개일 경우
if binary_search(weight):
    flag = True
# 물건이 2개일 경우
if not flag:
    start = 0
    end = stuff - 1
    
    while start < end:
        cur_sum = thing_list[start] + thing_list[end]
        if cur_sum == weight:
            flag = True
            break
        elif cur_sum > weight:
            end -= 1
        else:
            left_w = weight - cur_sum
            if left_w != thing_list[start] and left_w != thing_list[end]:
                if binary_search(left_w):
                    flag = True
                    break
            start += 1
if flag:
    print(1)
else:
    print(0)