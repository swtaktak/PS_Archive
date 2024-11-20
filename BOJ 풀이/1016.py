# sqrt(MAX) 이하의 소수를 모두 구하라.
# 그리고 그거의 제곱으로 떨어지면 끝
import sys
input = sys.stdin.readline

start, end = map(int, input().split())
prime_list = [True] * (int(end ** 0.5) + 3)
prime_list[0] = False
prime_list[1] = False
prime_range = []

for i in range(2, int(len(prime_list)**0.5) + 2):
    if prime_list[i]:
        for j in range(2*i, len(prime_list), i):
            prime_list[j] = False
            
for i in range(2, len(prime_list)):
    if prime_list[i]:
        prime_range.append(i)

num_list = [True] * (end - start + 1) # start부터 # end까지
square_nono = (end-start + 1)
for p in prime_range:
    # 이 부분도 에라토스테네스의 체로 구현
    cur_start = (start // p ** 2) * (p ** 2)
    for k in range(cur_start, end + 1, p ** 2):
        if k - start >= 0:
            # 방문한 적이 없다면 실패 처리
            if num_list[k - start]:
                num_list[k - start] = False
                square_nono -= 1
print(square_nono)
