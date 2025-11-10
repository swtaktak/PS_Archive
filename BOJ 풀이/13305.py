import sys
input = sys.stdin.readline

# idea : 일단 처음은 어쩔 수 없고, 더 싼 주유소를 만나면 교체해 버리자.

city = int(input())
dist_list = list(map(int, input().split()))
price_list = list(map(int, input().split())) # 사실 마지막은 의미가 없다.
ans = 0
min_oil = max(price_list) + 1 # 최솟값 초기 세팅

for i in range(city - 1):
    min_oil = min(min_oil, price_list[i])
    ans += (min_oil * dist_list[i])
print(ans)