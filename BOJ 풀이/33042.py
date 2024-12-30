import sys
input = sys.stdin.readline

N = int(input())
majak_dict = {}
is_error = False
majak_seq = list(map(str, input().rstrip().split()))
for i in range(N):
    m = majak_seq[i]
    if m not in majak_dict:
        majak_dict[m] = 1
    else:
        majak_dict[m] += 1
    if majak_dict[m] == 5:
        is_error = True
        print(i + 1)
        break
if not is_error:
    print(0)