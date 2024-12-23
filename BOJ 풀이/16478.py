import sys
input = sys.stdin.readline

pab, pbc, pcd = map(int, input().split())

pad = pab * pcd / pbc
print(pad)