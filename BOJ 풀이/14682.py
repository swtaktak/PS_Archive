# K + 1 개수만큼 1 붙는다. 그리고 곱한다.
import sys
input = sys.stdin.readline
N = int(input())
k = int(input())
mul = int('1' * (k+1))
print(N * mul)