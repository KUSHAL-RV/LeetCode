class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for row in board:
            arr1=[]
            r=set()    
            for cell in row:
                if cell != ".":
                    if cell in r:
                        return False
                    r.add(cell)
        for col in range(9):
            arr2=[]
            c=set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in c:
                        return False
                    c.add(board[row][col]) 
        for s_row in [0,3,6]:  
            for s_col in [0,3,6]:
                arr3=[]
                b=set()   
                for i in range(s_row,s_row+3):
                    for j in range(s_col,s_col+3):
                        if board[i][j]!=".":
                            if board[i][j] in b:
                                return False
                            b.add(board[i][j])
        return True




               

        

        

        




        







            