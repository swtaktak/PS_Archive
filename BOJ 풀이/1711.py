import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
point_list = []
for i in range(N):
    point_list.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    cur_dict = {}
    cx, cy = point_list[i][0], point_list[i][1]
    for j in range(N):
        if i != j:
            nx, ny = point_list[j][0] - cx, point_list[j][1] - cy
            if nx == 0:
                if (0, 1) not in cur_dict:
                    cur_dict[(0, 1)] = 1
                else:
                    cur_dict[(0, 1)] += 1
            elif ny == 0:
                if (1, 0) not in cur_dict:
                    cur_dict[(1, 0)] = 1
                else:
                    cur_dict[(1, 0)] += 1
            else:
                g = gcd(abs(nx), abs(ny))
                nx, ny = nx//g, ny//g
                if (nx, ny) not in cur_dict:
                    cur_dict[(nx, ny)] = 1
                else:
                    cur_dict[(nx, ny)] += 1
    # 내적이 0일 경우 그 값을 가져온다.
    coord_list = list(cur_dict.keys())
    for i in range(len(coord_list)):
        x, y = coord_list[i][0], coord_list[i][1]
        if (-y, x) in coord_list:
            answer += cur_dict[(x, y)] * cur_dict[(-y, x)]
        elif (y, -x) in coord_list:
            answer += cur_dict[(x, y)] * cur_dict[(y, -x)]
print(answer // 2)