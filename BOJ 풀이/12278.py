# 켤레의 성질 + 점화식을 활용하는 대수적 문제.
# 켤레 끼리는 제곱해도 서로 더해서 상쇄가 된다. (사실 근과 계수와의 관계 확장...)
# 점화식을 행렬곱으로 변형하는 테크닉이 필요.
p = 1000
def matrix_prod(m1, m2, p):
    x1 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % p
    x2 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % p
    x3 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % p
    x4 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % p
    return [[x1, x2], [x3, x4]]
def matrix_power_mod_p(matrix, n, p):
    if n == 0:
        return [[1, 0], [0, 1]]  
    elif n == 1:
        return matrix
    else:
        temp = matrix_power_mod_p(matrix, n//2, p)
        if n % 2 == 0:
            return matrix_prod(temp, temp, p)
        else:
            return matrix_prod(matrix_prod(temp, temp, p), matrix, p)
matrix = [[6, 996], [1, 0]] # 6 -4 0 1 이나 modulo를 위해. 
t_case = int(input())
for T in range(1, t_case+1):
    N = int(input())    # 초항 두개는 0항부터 2, 6 
    result_matrix = matrix_power_mod_p(matrix, N - 1, p)
    answer = (result_matrix[0][0] * 6 + result_matrix[0][1] * 2) - 1
    answer = answer % 1000
    if answer == 0:
        ansert = '000'
    elif len(str(answer)) == 1:
        answer = '00' + str(answer)
    elif len(str(answer)) == 2:
        answer = '0' + str(answer)
    else:
        answer = str(answer)
    
    print("Case #%d: %s" %(T, answer))
