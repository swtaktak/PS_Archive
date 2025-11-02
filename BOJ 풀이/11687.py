import sys
input = sys.stdin.readline

N = int(input())

result = 500000001
low = 1
upper = 5*N

while low <= upper:
    mid = (low + upper) // 2
    
    count = 0
    cur_check = mid
    while cur_check >= 5:
        count += cur_check // 5
        cur_check = cur_check // 5

    if count < N:
        low = mid + 1
    else:
        if count == N:
            if mid < result:
                result = mid
        upper = mid - 1

if result == 500000001:
    print(-1)
else:
    print(result)