import sys
input = sys.stdin.readline

def print_ans(ans):
    for i in range(rows):
        for j in range(cols):
            print(ans[i][j], end = " ")
        print()
rows, cols = map(int, input().split())
ones, nins = map(int, input().split())
answer = [[1 for _ in range(cols)] for _ in range(rows)]
# nins를 rows 개수만큼 서로 다른 자연수로 쪼갤 수 있는가?
# case 1 : rows가 cols보다 2개 이상 많다면? 불가능
if rows >= cols + 2:
    print(-1)
# case 2 : rows가 cols보다 정확히 1개 많다면?
elif rows == cols + 1:
    if nins == cols * (cols + 1) // 2:
        for i in range(rows):
            for j in range(cols):
                if i > j:
                    answer[i][j] = 9
        print_ans(answer)
    else:
        print(-1)
elif rows == 1:
    answer = [[1] * ones + [9] * nins]
    print_ans(answer)
else:
    min_nins = (rows * (rows - 1)) // 2
    max_nins = (rows * (2 * cols - rows + 1)) // 2
    if min_nins <= nins <= max_nins:
        # 추가로 채워줄 9의 개수
        add_nine = nins - min_nins
        # 각 줄별로 채울 9의 최대 개수
        max_add_nine = cols - rows + 1
        max_add_nine_row = add_nine // max_add_nine
        max_add_nine_rmd = add_nine % max_add_nine
        for i in range(rows):
            for j in range(cols):
                if i > j:
                    answer[i][j] = 9
        for i in range(rows-1, rows - max_add_nine_row -1, -1):
            for j in range(i, i + max_add_nine):
                answer[i][j] = 9
        for j in range(rows-max_add_nine_row-1, rows-max_add_nine_row-1 + max_add_nine_rmd):
            answer[rows-max_add_nine_row-1][j] = 9
        print_ans(answer)    
    else:
        print(-1)