a = int(input())
w, v = map(int, input().split())
if a * v <= w:
    print(1)
else:
    print(0)