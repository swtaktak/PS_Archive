import sys
input = sys.stdin.readline

find_len, cave_len = map(int, input().split())
find_s = str(input().rstrip())
cave_s = str(input().rstrip())

find_dict = {}
for c in find_s:
    if c not in find_dict:
        find_dict[c] = 1
    else:
        find_dict[c] += 1

answer = 0
start = 0
end = 0
cur_dict = {}
while end < cave_len:
    if end < find_len:
        if cave_s[end] not in cur_dict:
            cur_dict[cave_s[end]] = 1
        else:
            cur_dict[cave_s[end]] += 1
        end += 1
    else:
        if cave_s[end] not in cur_dict:
            cur_dict[cave_s[end]] = 1
        else:
            cur_dict[cave_s[end]] += 1
        end += 1
        
        cur_dict[cave_s[start]] -= 1
        if cur_dict[cave_s[start]] == 0:
            cur_dict.pop(cave_s[start])
        start += 1
    if cur_dict == find_dict:
        answer += 1

print(answer)