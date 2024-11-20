t_case = int(input())
for cur_case in range(1, t_case + 1):
    
    # 모든 방마다 번호가 붙여있고 다음 방과의 차이만 보면 되므로, 방문 체크할 이유는 없다.
    # x좌표나 y좌표를 넣어 줘야 한다.
    
    N = int(input())
    room_pos = [[-999, -999] for _ in range(N * N + 1)]
    for i in range(N):
        cur_row = list(map(int, input().split()))
        for j in range(len(cur_row)):
            # 좌표를 넣어준다.
            room_pos[cur_row[j]] = [i, j]
    # 시작 방부터 탐사를 시작한다.
    for i in range(1, N*N + 1):
        if i == 1:
            start_pos = 1
            enter_room = 1
            max_enter_room = 1
            max_start_pos = 1
        else:
            # 만일 좌우 연결일 경우 계속 가져가야함.
            px = room_pos[i-1][0]
            py = room_pos[i-1][1]
            cx = room_pos[i][0]
            cy = room_pos[i][1]
            # 범위를 벗어나는 것은 상관이 없다. 연결성만 체크하면 됨 연결시 방 수 + 1
            if [cx, cy] in [[px+1, py], [px-1, py], [px, py+1], [px, py-1]]:
                enter_room += 1
            else:
                # 끊겼을 때 최대 갱신 체크
                if enter_room > max_enter_room:
                    max_enter_room = enter_room
                    max_start_pos = start_pos
                # 초기화
                start_pos = i
                enter_room = 1
        # 마지막 완주 체크 해야함
        if enter_room > max_enter_room:
            max_enter_room = enter_room
            max_start_pos = start_pos
    print("#%d %d %d" %(cur_case, max_start_pos, max_enter_room))