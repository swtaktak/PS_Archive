import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
table = []
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    table.append(cur_row)
if min(rows, cols) == 1:
    print(1)
else:
    max_size = min(rows, cols)
    answer = 1
    
    for cur_size in range(max_size, 1, -1):
        cur_judge = False
        for r in range(0, rows - cur_size + 1):
            for c in range(0, cols - cur_size + 1):
                n1 = table[r][c]
                n2 = table[r][c + cur_size - 1]
                n3 = table[r + cur_size - 1][c + cur_size - 1]
                n4 = table[r + cur_size - 1][c]
                num_list = list(set([n1, n2, n3, n4]))
                
                if len(num_list) == 1:
                    answer = cur_size
                    cur_judge = True
                    break
            if cur_judge:
                break
        if cur_judge:
            break
    print(answer ** 2)
                