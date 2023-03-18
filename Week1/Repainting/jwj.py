def solution(n, m, section):
    answer = 0
    repaint = section[0]
    # section[0]에서부터 칠하는 횟수 카운트
    # 롤러 길이(m) + 안칠해진 다음 section부터 시작
    for i in section:
        if repaint <= i:
            repaint = i + m
            answer += 1
    return answer
