import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print('Scenario #%d:' %(i+1))
    result = (n+m)*(m-n+1)//2
    print(result)
    if i < t-1:
        print()