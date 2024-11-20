import sys
input = sys.stdin.readline

# 1과 -1을 활용하면 모든 경우를 만들 수 있다.
# num * 1을 반복하여 num보다 크게, num * -1 * -1을 하여 작게 가능.
t_case = int(input())
for _ in range(t_case):
    a, b = map(int, input().split())
    print('yes')