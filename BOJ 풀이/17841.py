import sys
input = sys.stdin.readline
P = 1000000007
N = int(input())
dp_table = [[0 for _ in range(5)] for _ in range(N)]
unist_char = 'UNIST'
unist = ['U', 'N', 'I', 'S', 'T']
for i in range(N):
    c = str(input().rstrip())
    # 초항 처리
    if i == 0:
        if c[0] == 'U':
            dp_table[i][0] = 1
            if len(c) >= 2 and c[:2] == 'UN':
                dp_table[i][1] = 1
                if len(c) >= 3 and c[:3] == 'UNI':
                    dp_table[i][2] = 1
                    if len(c) >= 4 and c[:4] == 'UNIS':
                        dp_table[i][3] = 1
                        if len(c) >= 5 and c[:5] == 'UNIST':
                            dp_table[i][4] = 1
    else:
        # 무조건 실패하는 케이스
        if c[0] not in unist:
            for j in range(5):
                dp_table[i][j] = dp_table[i-1][j]
        else:
            # 중도 문자열 실패를 고려하여 일단 세팅한다.
            for j in range(5):
                dp_table[i][j] = dp_table[i-1][j]
                
            # 첫자 U
            if c[0] == 'U':
                for k in range(0,5):
                    cur_char = unist_char[:k+1]
                    if len(c) >= k+1 and c[:k+1] == cur_char:
                        dp_table[i][k] = (dp_table[i][k] + 1) % P
                    else:
                        break
            else:
                start_idx = unist.index(c[0])
                for k in range(0, 5 - start_idx):
                    cur_char = unist_char[start_idx:start_idx+k+1]
                    if len(c) >= k+1 and c[:k+1] == cur_char:
                        dp_table[i][k + start_idx] = (dp_table[i][k + start_idx] + dp_table[i-1][start_idx-1]) % P
                    else:
                        break
        
print(dp_table[-1][4])