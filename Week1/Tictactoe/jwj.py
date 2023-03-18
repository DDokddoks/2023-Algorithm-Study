def solution(board):
    answer = -1
    O_cnt, X_cnt = 0, 0 # O의 개수, X의 개수
    O_line, X_line = 0, 0 # O와 X의 한줄 완성 개수

    # O와 X의 개수를 count
    for i in board:
        O_cnt += i.count('O')
        X_cnt += i.count('X')

    if O_cnt + X_cnt == 0:  # 아무것도 표시하지 않은 상태는 정상
        return 1
    if X_cnt > O_cnt:   # O가 선공이므로 X가 더 많으면 비정상
        return 0
    if O_cnt > X_cnt + 1:   # O가 선공이므로 X보다 1개 많을 수 있는데 더 많으면 비정상
        return 0

    # 대각선 \ 완성
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[1][1] == 'O':
            O_line += 1
        elif board[1][1] == 'X':
            X_line += 1

    # 대각선 / 완성
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[1][1] == 'O':
            O_line += 1
        elif board[1][1] == 'X':
            X_line += 1

    for i in range(3):
        # 세로 줄 완성 |
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[1][i] == 'O':
                O_line += 1
            elif board[1][i] == 'X':
                X_line += 1
        # 가로 줄 완성 ㅡ
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][1] == 'O':
                O_line += 1
            elif board[i][1] == 'X':
                X_line += 1

    # 완성된 O 줄이 없고 X 줄도 없을 때
    if O_line == 0 and X_line == 0:
        return 1
    # O 줄이 완성되고 X 줄은 완성되지 않았을 때, O의 개수가 X의 개수보다 1개 많다면 정상 (O 승리)
    if O_line > 0 and X_line == 0:
        if O_cnt > X_cnt:
            return 1
    # X 줄이 완성되고 O 줄은 완성되지 않았을 때, O와 X의 개수가 같다면 정상 (X 승리)
    if O_line == 0 and X_line > 0:
        if O_cnt == X_cnt:
            return 1
    # 그 외 모든 케이스는 잘못됨
    answer = 0
    return answer
