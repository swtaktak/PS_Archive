import sys
input = sys.stdin.readline

TEXT = input().rstrip()
PATTERN = input().rstrip()


def build_pi(pattern: str):
    """
    pi[suffix_end] =
        pattern[0..suffix_end]까지 봤을 때,
        '실패 시에도 유지 가능한 접두사(prefix) 길이'

    핵심 역할:
    - suffix_end : 접미 후보의 끝 인덱스 (오른쪽으로 하나씩 늘어남)
    - prefix_len : 현재까지 가능한 접두사 길이
    """
    m = len(pattern)
    pi = [0] * m

    prefix_len = 0  # 현재 유지 중인 접두사 길이

    # suffix_end를 오른쪽으로 늘려가며 확인
    for suffix_end in range(1, m):

        # 현재 접두사(prefix) 연장이 깨지면,
        # 더 짧은 접두사 후보로 내려가며 재시도
        while prefix_len > 0 and pattern[suffix_end] != pattern[prefix_len]:
            prefix_len = pi[prefix_len - 1]

        # 접두사 연장이 가능한 경우
        if pattern[suffix_end] == pattern[prefix_len]:
            prefix_len += 1
            pi[suffix_end] = prefix_len

    return pi


def kmp_search(text: str, pattern: str):
    """
    KMP 문자열 매칭

    핵심 원칙:
    - 텍스트(text)는 절대 뒤로 가지 않는다
    - 실패 시, 패턴(pattern)의 prefix_len만 pi를 이용해 점프한다
    """
    pi = build_pi(pattern)
    n, m = len(text), len(pattern)

    results = []

    prefix_len = 0  # 패턴에서 현재까지 맞춘 접두사 길이

    # 텍스트를 왼쪽 → 오른쪽으로 한 번만 순회
    for text_idx in range(n):

        # 현재 문자에서 패턴 연장이 실패하면,
        # prefix_len을 pi로 줄여가며 가능한 후보 탐색
        while prefix_len > 0 and text[text_idx] != pattern[prefix_len]:
            prefix_len = pi[prefix_len - 1]

        # 현재 문자가 맞으면 접두사 길이 증가
        if text[text_idx] == pattern[prefix_len]:
            prefix_len += 1

            # 패턴 전체가 매칭된 경우
            if prefix_len == m:
                # 시작 위치 기록 (문제 요구: 1-based index)
                results.append(text_idx - m + 2)

                # 겹치는 매칭을 위해
                # 패턴을 완전히 버리지 않고 pi로 점프
                prefix_len = pi[prefix_len - 1]

    return results


# 실행
matches = kmp_search(TEXT, PATTERN)
print(len(matches))
if matches:
    print(*matches)
