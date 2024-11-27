import sys
input = sys.stdin.readline

emozi = str(input().rstrip())
lens = len(emozi)
colons = emozi.count(':')
underba = emozi.count('_')

print(lens + colons + 5*underba)