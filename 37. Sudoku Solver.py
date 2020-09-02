'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.


Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    board[i][j] = int(board[i][j])
                else:
                    board[i][j] = 0
                    
        def return_empty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]==0:
                        return(i,j)
            return None
        
        def check(board,num,pos):
            row,col = pos
        
            # checking row
            for i in range(9):
                if board[row][i]==num and i!=col:
                    return False
        
            # checking col
            for i in range(9):
                if board[i][col]==num and i!=row:
                    return False
        
            # checking for sub-grid
            box_x = row//3
            box_y = col//3
        
            for i in range(box_x*3,box_x*3+3):
                for j in range(box_y*3,box_y*3+3):
                    if board[i][j]==num and (i,j)!=pos:
                        return False
            return True
        
        def solve(board):
            vacant = return_empty(board)
            if vacant is None:return True #means all cella are filled now and we have completed the sudoku
            row,col = vacant
            for i in range(1,10):
                if check(board,i,vacant):
                    board[row][col] = i
                    if solve(board):
                        return True
                    board[row][col] = 0
            return False
        
        solve(board)

        for i in range(9):
            l = ''
            for j in range(9):
                l+=str(board[i][j])
            board[i] = l
