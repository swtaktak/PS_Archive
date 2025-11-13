import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    sl, sr = map(str, input().rstrip().split())
    lup = 0
    rup = 0
    for i in range(len(sl)):
        if sl[i] == '0' and sr[i] == '1':
            rup += 1
        elif sl[i] == '1' and sr[i] == '0':
            lup += 1
    print(max(lup, rup))