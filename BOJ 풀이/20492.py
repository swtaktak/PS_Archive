import sys
input = sys.stdin.readline

N = int(input())

case1 = int(N * 0.78)
case2 = int(N - (N * 0.2 * 0.22))

print("%d %d"%(case1, case2))