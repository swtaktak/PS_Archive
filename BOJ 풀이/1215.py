import sys
input = sys.stdin.readline

def solve(n, k):
    ans = 0
    j = 0
    i = 1
    while i <= min(n, k):
        j = int(k / int (k / i))
        j = min(j, n)
        ans += (k // i) * (j - i + 1) * (i + j) // 2
        i = j + 1
    return ans

n, k = map(int, input().split())
print(n * k - solve(n, k))