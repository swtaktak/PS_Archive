import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    demand, station = map(int, input().split())
    print("%d %d" %(demand*station, demand//station))