import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cur_coin = int(input())
    coin_list = deque()
    for i in range(cur_coin):
        ctype, cnt = map(str, input().rstrip().split())
        coin_list.append([ctype, int(cnt)])
    coin_stack = []
    
    while coin_list:
        cur_type, cur_cnt = coin_list.popleft()
        # 코인 스택이 비거나, 코인의 맨 위가 현재 코인과 맞지 않아서 그냥 쌓아야 할 때
        if not coin_stack or cur_type != coin_stack[-1][0]:
            r = cur_cnt % 3
            q = cur_cnt // 3
            
            if r > 0:
                # 3개 미만나머지는 스택에 넣어서 잔여물을 등록한다. 
                coin_stack.append([cur_type, r])
            if q > 0:
                # 새로 만든 코인의 종류가 같냐, 다르냐에 따라 그냥 넣나 개수만 갱신
                if coin_list and coin_list[-1][0] == cur_type:
                    coin_list[-1][1] += q
                else:
                    coin_list.append([cur_type, q])
                    
        # 앞에 남은거랑 현재 코인 목록이랑 타입이 동일할 때.            
        else:
            # 잔여물의 이전과 합쳐서 나머지만 남기고 다 동전으로 제작.
            prev_cnt = coin_stack[-1][1]
            r = (cur_cnt+prev_cnt) % 3
            q = (cur_cnt+prev_cnt) // 3

            # 잔여 코인과 합쳐 처리한다.0개면 목록 자체에서 날린다.
            if r > 0:
                coin_stack[-1][1] = r
            else:
                coin_stack.pop()
            
            if q > 0:
                if coin_list and coin_list[-1][0] == cur_type:
                    coin_list[-1][1] += q
                else:
                    coin_list.append([cur_type, q])
    sum = 0
    for c in coin_stack:
        sum += c[1]
    print(sum)