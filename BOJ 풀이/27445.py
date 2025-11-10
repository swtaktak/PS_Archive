import sys
input = sys.stdin.readline

# 0이 있나 체크
# 0이 없으면 min min으로 idx 뽑아서 끝
row, col = map(int, input().split())
row_list = []

for _ in range(row - 1):
    n = int(input())
    row_list.append(n)
    
col_list = list(map(int, input().split()))
row_list.append(col_list[0])


# 행이나 열이 1인 경우가 걱정될 것이나, 어차피 0이 나오므로 zero를 구한다.

if 0 in row_list:
    ans_r = row_list.index(0) + 1
    ans_c = 1
    
elif 0 in col_list:
    ans_r = row
    ans_c = col_list.index(0) + 1
    
else:
    ans_r = row_list.index(min(row_list)) + 1
    ans_c = col_list.index(min(col_list)) + 1
    
print("%d %d" %(ans_r, ans_c))