import sys
no_hear, no_see = map(int, input().split())
no_hear_set = []
no_see_set = []
for i in range(0, no_hear):
    no_hear_set.append(str(sys.stdin.readline().rstrip()))
for i in range(0, no_see):
    no_see_set.append(str(sys.stdin.readline().rstrip()))
no_hear_see = list(set(no_hear_set) & set(no_see_set))
no_hear_see.sort()

print(len(no_hear_see))
for n in no_hear_see:
    print(n)