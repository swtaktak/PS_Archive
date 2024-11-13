import sys
input = sys.stdin.readline
# 0이 흰색, 1이 파란색
def cut_paper(x, y, N):
    global white, blue
    start_color = paper[x][y]
    
    # 현재 조각의 색종이가 전부 동일한가?
    for i in range(x, x+N):
        for j in range(y, y+N):
            # 특정 지점에서 동일하지 않다면
            # 그 지점에서 색종이를 잘라, 사분면을 확인한다.
            # 확인 뒤에 같지 않은 지점이 나오면 색종이 장 수를 더 하면 안된다.
            # 그래서 return을 붙인다.
            if paper[i][j] != start_color:
                cut_paper(x, y, N//2)
                cut_paper(x + N//2, y, N//2)
                cut_paper(x, y + N//2, N//2)
                cut_paper(x + N//2, y + N//2, N//2)
                return
    if start_color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = []
for i in range(N):
    cur_line = list(map(int, input().split()))
    paper.append(cur_line)

start_x = 0
start_y = 0
white = 0
blue = 0
cut_paper(0, 0, N)
print(white)
print(blue)