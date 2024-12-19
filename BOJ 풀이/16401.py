import sys
input = sys.stdin.readline

def count_cousin(cur_c, c_list):
    answer = 0
    for c in c_list:
        answer += (c // cur_c)
    return answer

cousin, cookie = map(int, input().split())
c_list = list(map(int, input().split()))

answer = 0
left = 1
right = max(c_list)

if cousin > sum(c_list):
    print(0)
else:
    while left <= right:
        mid = (left + right) // 2
        cur_cousin = count_cousin(mid, c_list)
        if  cur_cousin < cousin:
            right = mid - 1
        
        else:
            if answer < mid:
                answer = mid
            left = mid + 1
    print(answer)