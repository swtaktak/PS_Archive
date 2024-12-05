import sys
input = sys.stdin.readline
N, K = map(int, input().split())

# 애초부터 불가능.
if N <= K:
    print(0)
# 완전 그래프 케이스 (사실 홀짝성에서 안따져도 되지만..)
elif N-1 == K:
    print(N)
# 점이 짝수거나 차수가 짝수면 무조건 가능
elif N % 2 == 0 or K % 2 == 0:
    print(N)
# 차수가 홀수고, 점도 홀수면 점 하나 버려라.
# 위에서 이미 불가능 케이스를 보려서 점은 차수보다 최대 2개 많아 점 하나 버려도 모순 없음.
else:
    print(N-1)