import sys
input = sys.stdin.readline

P = int(input())

for cur_practice in range(1, P+1):
    student, brownie = map(int, input().split())
    # 브라우니는 항상 학생보다 많아야 한다;.
    print("Practice #%d: %d %d" %(cur_practice, student, brownie))
    groups = int(input())
    for _ in range(groups):
        cur_mem = int(input())
        while cur_mem >= brownie:
            brownie *= 2
        left_brownie = brownie - cur_mem
        print("%d %d" %(cur_mem, left_brownie))
        brownie = left_brownie
    print()