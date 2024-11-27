import sys
input = sys.stdin.readline

origin, rows, cols = map(int, input().split())
answer = ['?'] * origin

notes = []
for _ in range(rows):
    notes.append(str(input().rstrip()))

for i in range(rows):
    for j in range(0, origin*cols, cols):
        # 현재 문자열을 찾는다.
        cur_str = notes[i][j:j+cols]
        cur_letter = '?'
        for c in cur_str:
            if c.isalpha():
                cur_letter = c
        if cur_letter != '?':
            answer[j // cols] = cur_letter
print(''.join(answer))