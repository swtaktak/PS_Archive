min_q, max_q = map(int, input().split())
bs_solved, bs_error = map(int, input().split())

lower_bound = max(bs_solved - bs_error, min_q)
upper_bound = min(bs_solved + bs_error, max_q)
friend = upper_bound - lower_bound + 1

if friend >= 1:
    print(friend)
else:
    print("IMPOSSIBLE")