# 가희와 탑 문제
# 가장 최근의 건물 정보를 줄려면?
# 최대한 그리디하게 생각해야 한다.
# N층을 우측에 가장멀리 박고
# N-1 N-2 N-3 N-4 를 왼쪽에 박고
# 나머지를 왼쪽에서 만족한다.
# 이때 가장 작은거부터 해야 한다.
# 나머지도 계단으로 챙긴다
# 즉 1 2 ..(좌측제일큼)  탑 아래..... N N-1 N-2 is best
# 불가능은? 2개 이상일때 11이거나 L + R > N 일때 불가능

import sys
input = sys.stdin.readline

N, left, right = map(int, input().split())

if N == 1:
    if left == 1 and right == 1:
        print(1)
    else:
        print(-1)
elif N == 2:
    if left == 1 and right == 2:
        print('2 1')
    elif left == 2 and right == 1:
        print('1 2')
    elif left == 1 and right == 1:
        print('1 1')
    else:
        print(-1)
else:
    if left + right > N + 1:
        print(-1)
    else:
        # 문제 : 같은 건물 층수가 나올 수 있어서 문제임.
        # 우측에서 보여야 하는 건물 개수 최종 지점에, 좌측에서 보이는 건물 최대 개수를 박으면 그만
        # 거기서부터 왼쪽은 반대로 채우고 싹다 1로 채움
        # 우측은 뒤에서 1부터 채우면 됨?
        # 2 4 는 1 4 3 2 1 로 채워야함.
        # 둘 중 더 큰거로 채우면 됨..
        
        core = left + right - 1
        
        ans_list = [1 for _ in range(core)]
        ans_list[core - right] = max(left, right)
        
        # 우측 채우기 : 우측 할당량을 채워야 함
        cur_right_see = 2
        for idx in range(core - right + 1, core):
            if cur_right_see < right:
                ans_list[idx] += right - cur_right_see
                cur_right_see += 1
                
        cur_left_see = 2
        for idx in range(core-right-1, -1, -1):
            if cur_left_see < left:
                ans_list[idx] += left - cur_left_see
                cur_left_see += 1
                
        while len(ans_list) < N:
            ans_list.insert(1, 1)
        
        for a in ans_list:
            print(a, end = " ")