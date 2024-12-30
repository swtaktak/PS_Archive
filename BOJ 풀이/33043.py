import sys
input = sys.stdin.readline

N = int(input())
majak_dict = {}
is_error = False
majak_seq = list(map(str, input().rstrip().split()))
memory_need = N + 1

start = 0
end = 0
while end < N:
    m = majak_seq[end] # 현재 확인 패
    if m not in majak_dict:
        majak_dict[m] = 1
    else:
        majak_dict[m] += 1
    while majak_dict[m] >= 5:
        is_error = True
        memory_need = min(memory_need, end - start + 1)
        s = majak_seq[start]
        majak_dict[s] -= 1
        start += 1
    end += 1
if is_error:
    print(memory_need)
else:
    print(-1)