import sys
input = sys.stdin.readline

# 패딩은 36으로 실시
# 0~25 알파벳 26~35 영어 대문자, 36은 패딩
cypher_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z',
               '0', '1', '2', '3', '4',
               '5', '6', '7', '8', '9', ' ']
N = int(input())
matrix = []
for i in range(N):
    cur_row = list(map(int, input().split()))
    matrix.append(cur_row)

plain_text = str(input().rstrip())

# 패딩 작업 공백 실시
while len(plain_text) % N != 0:
    plain_text += " "

answer = ""
for i in range(0, len(plain_text), N):
    cur_step_text = plain_text[i:i+N]
    cur_col = []
    for c in cur_step_text:
        cur_col.append(cypher_list.index(c))
    matrix_result = []
    for i in range(N):
        temp = 0
        for j in range(N):
            temp += matrix[i][j] * cur_col[j]
        matrix_result.append(temp % 37) 
    for m in matrix_result:
        answer += cypher_list[m]
print(answer)