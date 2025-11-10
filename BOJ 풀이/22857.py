import sys
input = sys.stdin.readline

N, cutline = map(int, input().split())
num_list = list(map(int, input().split()))
                
left, right = 0, 0
answer, now_len = 0, 0

while right < N:
    if num_list[right] % 2 == 0:
        now_len += 1
        right += 1
        answer = max(answer, now_len)
    else:
        if cutline > 0:
            cutline -= 1
            right += 1
        else:
            if num_list[left] % 2 == 0:
                now_len -= 1
                left += 1
            else:
                cutline += 1
                left += 1
print(answer)