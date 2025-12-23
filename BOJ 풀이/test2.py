# 백준에서는 입력을 빠른 입력을 받아야 한다
# 그냥 이거 치고 무조건 시작
import sys
input = sys.stdin.readline

a, b = map(int, input().split()) # 공백 있는 숫자 목록 받는 방법
print(a + b)