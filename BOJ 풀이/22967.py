import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# case 1) N = 2
if N == 2:
    l, r = map(int, input().split())
    # 문제 조건 때문에 1개를 받기는 하나, 이거로 충분.
    print(0) # 0개 추가
    print(1) # 거리는 1
    
elif N <= 4:
    # 3, 4의 경우는 완전그래프가 된다.
    # 즉, 그래프에 다가 박고 완전이 아닌 것들을 세서 모두 넣어준다.
    for _ in range(N-1):
        l, r = map(int, input().split())
        graph[l][r] = 1
        graph[r][l] = 1
        
    
    ans_list = []
    # 추가 다리 수
    if N == 3:
        print(1)
    elif N == 4:
        print(3)
    # 반지름. 완전 그래프이므로 1
    print(1)
    
    for l in range(1, N+1):
        for r in range(l+1, N+1):
            if graph[l][r] == 0:
                ans_list.append((l, r))
    for a in ans_list:
        print("%d %d" %(a[0], a[1]))

else:
    # 5 이상 부터는 N(N-1)/2 >2(N-1)  (N>4 부터는 거리 1 확정적 불가)
    # 거리 2를 확보하기 위해서는 하나에 모든 것이 연결되어야 한다.
    # 1번에다가 다 연결한다. 1번과 연결되어 있지 않은 애들을
    
    for _ in range(N-1):
        l, r = map(int, input().split())
        graph[l][r] = 1
        graph[r][l] = 1
        
    ans_list = []
    cnt = 0
    for i in range(2, N+1):
        if graph[1][i] == 0:
            cnt += 1
            ans_list.append((1, i))
    print(cnt)
    print(2)
    
    for a in ans_list:
        print("%d %d" %(a[0], a[1]))