# 9753
import sys
input = sys.stdin.readline

MAX = 100000
prime_judge = [True for _ in range(MAX + 1)]
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_judge[i]:
        for j in range(i * i, MAX + 1, i):
            if prime_judge[j]:
                prime_judge[j] = False
prime_list = []
for p in range(2, MAX + 1):
    if prime_judge[p]:
        prime_list.append(p)


# 그냥 다 소인수분해를 하는 행위는 무리
# 이분탐색이 나음
# p * q >= K 가 되는 최소의 pq를 찾아야 함.
# p보다 큰 q라고 wlog라고정의해도 됨

T = int(input())
for _ in range(T):
    K = int(input())
    
    # 예제을 보고 최대 값을 100002로 고정
    # 사유 : 최대 범위인 100000의 정답이 100001이라 이거보다 안큼
    ans = 100002
    for i in range(len(prime_list)):
        p = prime_list[i]
        
        # idx 기준임
        left = i + 1
        right = len(prime_list) - 1
        if p * prime_list[left] > ans:
            break
        
        while left <= right:
            mid = (left + right) // 2
            q = prime_list[mid]
            if p * q < K:
                left = mid + 1
            else:
                ans = min(ans, p * q)
                right = mid - 1
    print(ans)