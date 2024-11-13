import sys
input = sys.stdin.readline

fruit = int(input())
tanghuru = list(map(int, input().split()))

left = 0
right = 0
max_len = 0
tanghuru_dict = {}
f_type = 0
while right < fruit:
    # 다음 칸을 넣고 생각한다.
    if tanghuru[right] not in tanghuru_dict:
        f_type += 1
        tanghuru_dict[tanghuru[right]] = 1
    else:
        tanghuru_dict[tanghuru[right]] += 1
    
    # 만일 3개 이상의 종류가 존재한다면
    # 왼쪽에서 순서대로 뺀다.
    while f_type >= 3:
        tanghuru_dict[tanghuru[left]] -= 1
        if tanghuru_dict[tanghuru[left]] == 0:
            f_type -= 1
            del tanghuru_dict[tanghuru[left]]
        left += 1
        
    right += 1
    max_len = max(max_len, right- left)
print(max_len)