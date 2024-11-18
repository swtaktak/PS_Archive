import sys
input = sys.stdin.readline
row_str = str(input().rstrip()) # 세로줄에 배치들어감
col_str = str(input().rstrip()) # 가로줄에 배치들어감
rows = len(row_str)
cols = len(col_str)
dp = [[0 for _ in range(cols)] for _ in range (rows)]

for i in range(rows):
    for j in range(cols):
        # 맨 첫줄 세로 줄 글자랑 같은 시점부터 쭉 1로 배치함.  가져오면 됨
        if i == 0:
            if j == 0:
                if row_str[0] == col_str[0]:
                    dp[0][0] = 1
                else:
                    dp[0][0] = 0
            else:
                if row_str[0] == col_str[j]:
                    dp[0][j] = 1
                else:
                    dp[0][j] = dp[0][j-1]
        else:
            # 두 번째 세로줄 부터
            # 가로 방향의 첫 글자일 경우
            if j == 0:
                if row_str[i] == col_str[0]:
                    dp[i][0] = 1
                else:
                    dp[i][0] = dp[i-1][0]
            else:
                # 열에 글자가 추가되어 같아진 거니까.
                if row_str[i] == col_str[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 앞에서 늘어나는 경우를 고려하자. 둘 중 더 큰걸 기억한다.(그럼 잘 누적됨.)
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])