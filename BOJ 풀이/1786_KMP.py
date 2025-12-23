# 1786
# KMP 입문 문제

import sys
input = sys.stdin.readline

text = input().rstrip()
pattern = input().rstrip()


# step 1. 패턴에서 실패 함수를 만든다.
# 실패함수의 역할은, 매칭이 안되었을 시 유지 가능한 접두사를 찾는다.
# suffix_end : 접미 후보의 마지막 인덱스
# prefix_len : 현재 까지 가능한 접두사

def build_failure(pattern):
    m = len(pattern)
    fail = [0] * m
    
    prefix_len = 0 # 현재 유지(일치) 중인 접두사의 길이
    
    for suffix_end in range(1, m):
        
        while prefix_len > 0 and pattern[suffix_end] != pattern[prefix_len]:
            # 접미와 접두가 불일치시, 더 짧은 후보로 내려가서 시도해야 한다.
            # Question. 그러면 접두를 하나 줄이지, 왜 굳이 fail에서 찾음?
            # 어차피 앞에서 불일치하는 양을 굳이 찾지 않고, 일치하는 양만을 가져온다.
            # 계속 불일치하면 계속 줄여야한다.
            prefix_len = fail[prefix_len - 1]
            
        # 접두사의 연장이 가능하다.
        if pattern[suffix_end] == pattern[prefix_len]:
            prefix_len += 1
            fail[suffix_end] = prefix_len
    return fail

# 실패시 패턴의 prefix_len만 pi를 활용하여 점프
# 전체 다 일치해야만 통과
def kmp_search(text, pattern):
    fail = build_failure(pattern)
    n, m = len(text), len(pattern)
    
    results = []
    prefix_len = 0 # 현재까지 맞힌 접두사의 길이
    
    for text_idx in range(n):
        while prefix_len > 0 and text[text_idx] != pattern[prefix_len]:
            # 패턴 일치가 안 될 경우, 길이를 1 줄인 뒤 일치하는 양을 가져옴
            prefix_len = fail[prefix_len - 1]
        
        # 한 글자 일치
        if text[text_idx] == pattern[prefix_len]:
            prefix_len += 1
            
            if prefix_len == m:
                # 1-base로 수정해야함. m까지 다 돌아버려서 시작점 찾기
                results.append(text_idx - m + 2)
                # 다음 문자열에서 겹치는 분량을 사용하기 위해
                prefix_len = fail[prefix_len - 1]
    return results

match_result = kmp_search(text, pattern)
print(len(match_result))
if match_result:
    for m in match_result:
        print(m, end = " ")