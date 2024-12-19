import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    num_a, num_b = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    
    list_a.sort(reverse = True)
    list_b.sort()
    
    answer = 0
    for cur_a in list_a:
        if not list_b:
            break
        while list_b and list_b[-1] >= cur_a:
            list_b.pop()
            num_b -= 1
        answer += num_b
    print(answer)