def solution(board):
    winO, winX, cntO, cntX = 0, 0, 0, 0
    
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O': winO += 1
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O': winO += 1
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X': winX += 1
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X': winX += 1
    
    
    for i in range(3):
        if board[i] == "OOO": winO += 1
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O': winO += 1
        if board[i] == "XXX": winX += 1
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X': winO += 1
        
        cntO += board[i].count('O')
        cntX += board[i].count('X')
    
    if cntX > cntO: return 0 
    if cntO - 2 >= cntX: return 0
    if winO > 0 and winX > 0: return 0
    if winO > 0 and cntO <= cntX: return 0
    if winX > 0 and cntO > cntX: return 0
    
    return 1


print(solution(["...", ".X.", "..."]))
