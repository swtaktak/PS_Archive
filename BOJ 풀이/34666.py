import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    kyu, lang, read, listen = map(int, input().split())
    
    judge = True
    
    # 조건 1 탈락
    if kyu >= 3:
        judge = False
    
    # 조건 2 탈락
    elif listen < 50:
        judge = False
    
    else:
        condi_3 = False
        if kyu == 2:
            if lang * 3 < 90 and read * 3 < 90:
                condi_3 = True
            if lang <= 21 or read <= 21:
                condi_3 = True            
        elif kyu == 1:
            if lang * 3 < 100 and read * 3 < 100:
                condi_3 = True
            if lang <= 21 or read <= 21:
                condi_3 = True
        if not condi_3:
            judge = False
    if judge:
        print('YES')
    else:
        print('NO')
