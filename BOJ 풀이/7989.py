import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    ans = int(input())
elif N == 2:
    a = int(input())
    b = int(input())
    ans = max(a, b)
else:
    ans = 0
    num_list = []
    for _ in range(N):
        num_list.append(int(input()))
    num_list.sort()
    # idea : first, second가 뺑이질 칠거임
    first = num_list[0]
    second = num_list[1]
    
    while N > 3:
        max1 = num_list.pop()
        max2 = num_list.pop()
        # 최저 시간이 뺑이질 더 칠거니,  둘이 같이 뺑이질 칠거니
        ans += min(2*first + max1 + max2,  first + 2*second + max1)
        N -= 2
            
    if len(num_list) == 2:
        ans += second
    elif len(num_list) == 3:
        ans += (max(num_list) + first + second)
print(ans)