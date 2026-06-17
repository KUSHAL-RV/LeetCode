class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        c=set()
        a=0
        
        arr2=[]

        for row in board:
            arr1=[]
            r=set()
            
            for cell in row:
                if cell != ".":
                    arr1.append(cell)
                    r.add(cell) 
            
            if len(arr1) != len(r):
                return False

        for col in range(9):
            arr2=[]
            c=set()

            for row in range(9):
                if board[row][col] != ".":
                    arr2.append(board[row][col])
                    c.add(board[row][col]) 
                
            if len(arr2) != len(c):
                return False

        for s_row in [0,3,6]:
                
            for s_col in [0,3,6]:
                arr3=[]
                b=set()
                    
                for i in range(s_row,s_row+3):
                    for j in range(s_col,s_col+3):
                        if board[i][j]!=".":
                            arr3.append(board[i][j])
                            b.add(board[i][j])

                if len(arr3) != len(b):
                    return False
        return True




               

        

        

        




        







            