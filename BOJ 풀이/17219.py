import sys
input = sys.stdin.readline

join_site, find_site = map(int, input().split())
pw_dict = {}
for _ in range(join_site):
    cur_site, cur_pw = map(str, input().rstrip().split())
    pw_dict[cur_site] = cur_pw

for _ in range(find_site):
    find_site = str(input().rstrip())
    print(pw_dict[find_site])