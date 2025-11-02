import sys
input = sys.stdin.readline

visited = [True for _ in range(1000)]
N = int(input())

# step 1 : 범위 벗어나며 아닌거
for i in range(1000):
    if i < 100:
        visited[i] = False
    else:
        si = str(i)
        if '0' in si:
            visited[i] = False
        if si[0] == si[1] or si[0] == si[2] or si[1] == si[2]:
            visited[i] = False
            
# step 2 : check
for _ in range(N):
    cur_num, cur_s, cur_b = map(int, input().split())
    scn = str(cur_num)
    for cur_check in range(123, 1000):
        if visited[cur_check]:
            chk_s, chk_b = 0, 0
            schk = str(cur_check)
            if schk[0] == scn[0]:
                chk_s += 1
            elif schk[0] == scn[1] or schk[0] == scn[2]:
                chk_b += 1
                
            if schk[1] == scn[1]:
                chk_s += 1
            elif schk[1] == scn[0] or schk[1] == scn[2]:
                chk_b += 1
                
            if schk[2] == scn[2]:
                chk_s += 1
            elif schk[2] == scn[0] or schk[2] == scn[1]:
                chk_b += 1
            
            if chk_s != cur_s or chk_b != cur_b:
                visited[cur_check] = False

# step 3 : answer cnt
ans = 0
for i in range(123, 1000):
    if visited[i]:
        ans += 1
print(ans)