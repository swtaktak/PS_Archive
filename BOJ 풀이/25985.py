# 비례식과 방정식 문제
# zero issue 없음

A, B = map(int, input().split())
before = A
after = (A*B-100*B) / (B - 100)

print(before/after)