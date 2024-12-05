import sys
input = sys.stdin.readline
def check_list(cur_s):
    # 모든 체크 리스트 원소를 주고 정렬한다.
    chk_list = []
    cur_s = str(cur_s)
    max_len = len(cur_s)
    for digit in range(1, max_len):
        for j in range(0, max_len - digit + 1):
            chk_list.append(int(cur_s[j:j+digit]))
    cur = list(set(sorted(chk_list)))
    if 0 in cur:
        cur = cur[1:]
    return cur

N = int(input())
dp = [-1] * (N+1)
for i in range(1, N+1):
    if i < 10:
        # 자기 자신은 패배이므로 한 자리수는 무조건 패배한다.
        dp[i] = -1
    else:
        cur_check = check_list(i)
        for c in cur_check:
            if i - c <= 1:
                break
            else:
                if dp[i-c] == -1:
                    dp[i] = c
                    break
print(dp)
print(dp[-1])