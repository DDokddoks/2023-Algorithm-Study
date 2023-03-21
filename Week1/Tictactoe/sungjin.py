def solution(board):
    answer = 0
    XCount = 0
    OCount = 0
    Xline = 0
    Oline = 0
    
    for i in range(3):
        XCount += board[i].count('X')
        OCount += board[i].count('O')
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                Xline += 1
            elif board[i][0] == 'O':
                Oline += 1
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                Xline += 1
            elif board[0][i] == 'O':
                Oline += 1
        
    #대각선 확인
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            Xline += 1
        elif board[0][0] == 'O':
            Oline += 1
    if board[0][2] == board [1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            Xline += 1
        elif board[0][2] == 'O':
            Oline += 1
    
    #X가 더 많거나 O가 X보다 2개 이상 차이나면
    if XCount > OCount:
        return 0
    elif OCount - XCount >= 2:
        return 0
    
    #하나 놨을 때 여러줄 완성될수 있음
    if Oline == 0 and Xline == 0:
        answer = 1
    if Oline > 0 and Xline == 0:
        answer = 1
    if Oline == 0 and Xline > 0 and (XCount ==0 and OCount ==0):
        answer = 1
    answer = 0

    return answer

# 1. X가 O보다 많음
# 2. 빙고가 여러개임
# 3. O와 X차이가 2이상임