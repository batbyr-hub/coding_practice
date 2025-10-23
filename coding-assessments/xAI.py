class Solution(object):

    # [
    #   ['#', '-', '#', '#', '*'],
    #   ['#', '-', '-', '#', '#'],
    #   ['-', '#', '-', '#', '-'],
    #   ['-', '-', '#', '-', '#'],
    #   ['#', '*', '-', '-', '-'],
    #   ['-', '-', '*', '#', '-']
    # ]

    def matrixBoard(board):
        for i in range(len(board), -1, -1):
            for j in range(len(board)):
                # if board[i][j] == '*':
                #     board[i][j] = '-'
                print(board[i][j])
