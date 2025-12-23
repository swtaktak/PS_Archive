import sys
import heapq
input = sys.stdin.readline

K, N = map(int, input().split())      
primes = list(map(int, input().split()))
hq = primes[:]     
heapq.heapify(hq)

ans = 0
for _ in range(N):
    cur = heapq.heappop(hq)  
    ans = cur

    for p in primes:
        heapq.heappush(hq, cur * p)

        if cur % p == 0:
            # cur의 가장 작은 소인수가 p 이므로
            # 더 큰 소수들로 곱해서 만들 수 있는 애들은
            # 이미 다른 루트에서 생성될 애들은 여기서 더 안 만든다
            break

print(ans)
