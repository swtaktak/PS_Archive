import sys
input = sys.stdin.readline

def check(pos):
    flag = True
    for i in range(0, N, 2):
        word1 = word_list[i]
        word2 = word_list[i+1]
        if word1[:pos] != word2[:pos]:
            flag = False
            break
    return flag

N = int(input())
word_list = []
for _ in range(N):
    w = str(input().rstrip())
    word_list.append(w)
word_list.sort()

max_len = len(w)

start = 0
end = max_len
ans = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1
print(ans)