import sys
input = sys.stdin.readline

N = int(input())
al = []
bl = []
cl = []
dl = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)
    dl.append(d)
    
abl = {}

for a in al:
    for b in bl:
        if a+b not in abl:
            abl[a+b] = 1
        else:
            abl[a+b] += 1

answer = 0
for c in cl:
    for d in dl:
        if -(c+d) in abl:
            answer += abl[-(c+d)]
print(answer)