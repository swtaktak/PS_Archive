import sys
import copy
input = sys.stdin.readline

def get_det(mat):
    term1 = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
    term2 = mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
    term3 = mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
    return term1 - term2 + term3

T = int(input())
for _ in range(T):
    mat = []
    y = []
    det_list = []
    for _ in range(3):
        a, b, c, d = map(int, input().split())
        mat.append([a, b, c])
        y.append(d)

    for i in range(3):
        new_mat = copy.deepcopy(mat)
        for j in range(3):
            new_mat[j][i] = y[j]
        cur_det = get_det(new_mat)
        det_list.append(cur_det)

    det_list.append(get_det(mat))

    print(" ".join(map(str, det_list)))

    if det_list[3] == 0:
        print("No unique solution")
    else:
        ans_list = []
        for i in range(3):
            value = det_list[i] / det_list[3]
            formatted_value = f"{value:.3f}" if abs(value) >= 0.0005 else "0.000"
            ans_list.append(formatted_value)
        print("Unique solution:", " ".join(ans_list))
    print()