import sys
input = sys.stdin.readline

S = str(input().rstrip())
T = str(input().rstrip())

print(S + S[-1])