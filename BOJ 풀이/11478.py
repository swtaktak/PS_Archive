import sys
input = sys.stdin.readline
s = str(input().rstrip())
subset = set()

for left in range(0, len(s)):
    for right in range(1, len(s) + 1):
        if left < right:
            sub_s = s[left:right]
            subset.add(sub_s)
print(len(subset))