# 이 방법으론 어렵고.. binary가 맞다.

target, start, end = map(int, input().split())
answer = 0
if target % 2 == 0:
    if start <= end <= target:
        