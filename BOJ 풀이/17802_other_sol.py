import sys
input = sys.stdin.readline
line, N = map(int, input().split())
if line == 1:
    print(N)
else:
    if 2 ** (line - 1) > N:
        print('impossible')
    else:
        ans = [[] for _ in range(line)]
        first_num = N - (2 ** (line - 1) - 1)
        ans[0].append(first_num)
        for _ in range(line - 1):
            ans[0].append(1)
        
        # 이제 순서대로 합치자.
        for i in range(1, line):
            # i-1 floor에 대해서 합친다.
            for j in range(1, line - i + 1):
                ans[i].append(ans[i-1][j] + ans[i-1][j-1])
        
        for cur_row in ans[::-1]:
            for c in cur_row:
                print(c, end = " ")
            print()