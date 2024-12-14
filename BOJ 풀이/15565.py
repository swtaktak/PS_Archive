import sys
input = sys.stdin.readline
dolls, cutline = map(int, input().split())
doll_list = list(map(int, input().split()))
start = 0
end = 0
cur_lion = 0
ans = 1e9
while end <= dolls:
    if cur_lion == cutline:
        ans = min(ans, end - start)
        if doll_list[start] == 1:
            cur_lion -= 1
        start += 1
    else:
        if end < dolls and doll_list[end] == 1:
            cur_lion += 1
        end += 1
if ans == 1e9:
    print(-1)
else:
    print(ans)