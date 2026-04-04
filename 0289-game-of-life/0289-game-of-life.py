import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        matrix = copy.deepcopy(board)
        col = len(board[0])
        row = len(board)
        for i in range(row):
            
            for j in range(col):
                live = 0
                #top
                if(i>0 and j!=0):
                    if(matrix[i-1][j-1]==1):
                        live+=1
                        
                if(i>0 and j<col-1):
                    if(matrix[i-1][j+1]==1):
                        live+=1
                        
                if(i>0):
                    if(matrix[i-1][j]==1):
                        live+=1
                        
                
                #left
                if(j>0 and i<row-1):
                    if(matrix[i+1][j-1]==1):
                        live+=1
                        
                if(j>0):
                    if(matrix[i][j-1]==1):
                        live+=1
                        
                
                #right
                if(j<col-1 and i<row-1):
                    if(matrix[i+1][j+1]==1):
                        live+=1
                        
                if(j<col-1):
                    if(matrix[i][j+1]==1):
                        live+=1
                        
                
                #down
                if(i<row-1):
                    if(matrix[i+1][j]==1):
                        live+=1

                #checking
                if(board[i][j]==1):
                    if (live<2 or live>3):
                        board[i][j]=0
                else:
                    if(live==3):
                        board[i][j]=1        
            

                
                
                    


        