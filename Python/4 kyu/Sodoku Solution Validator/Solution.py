def validSolution(board):
    for row in board:
        nums = []
        for num in row:
            if num > 9 or num < 1:
                return False
            else:
                if not num in nums:
                    nums.append(num)
                else:
                    return False

    for i in range(0,3):
        section = []
        for k in range(0, 9):
            for j in range (i*3,i*3+3):
                if not board[k][j] in section:
                    section.append(board[k][j])
                else:
                    return False
            if((k+1)%3 == 0):
                section = []
        
    for i in range(0,9):
        column = []
        for j in range(0,9):
            if not board[j][i] in column:
                column.append(board[j][i])
            else:
                return False

    return True
