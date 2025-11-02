import sys
import heapq
# 상대방이 말한소수수
input = sys.stdin.readline

prime_list = [True] * 5000001
prime_list[0] = False
prime_list[1] = False
for i in range(2, int(5000001 ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2*i, 5000001, i):
            prime_list[j] = False
visited = [False] * 5000001

daeung, kyuseong = 0, 0
total_r = int(input())
call_list_dae = []
call_list_kyu = []

for _ in range(total_r):
    cr, ck = map(int, input().split())
    if not prime_list[cr]:
        if len(call_list_kyu) < 3:
            kyuseong += 1000
        else:
            score = heapq.heappop(call_list_kyu)
            kyuseong += score
            heapq.heappush(call_list_kyu, score)
    elif visited[cr]:
        daeung -= 1000
    else:
        visited[cr] = True
        heapq.heappush(call_list_dae, cr)
        if len(call_list_dae) >= 4:
            heapq.heappop(call_list_dae)
            
            
        
    if not prime_list[ck]:
        if len(call_list_dae) < 3:
            daeung += 1000
        else:
            score = heapq.heappop(call_list_dae)
            daeung += score
            heapq.heappush(call_list_dae, score)
    elif visited[ck]:
        kyuseong -= 1000
    else:
        visited[ck] = True
        heapq.heappush(call_list_kyu, ck)
        if len(call_list_kyu) >= 4:
            heapq.heappop(call_list_kyu)
            
if daeung > kyuseong:
    print('소수의 신 갓대웅')
elif daeung < kyuseong:
    print('소수 마스터 갓규성')
else:
    print('우열을 가릴 수 없음')