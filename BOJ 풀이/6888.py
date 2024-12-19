# lcm(2, 3, 4, 5) = 60
import sys
input = sys.stdin.readline
X = int(input())
Y = int(input())

for i in range(X, Y+1, 60):
    print("All positions change in year %d" %(i))