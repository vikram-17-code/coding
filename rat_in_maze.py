
def maze(arr,size):
    status = False
    
    def checker(array,i,j):
        nonlocal status
        if status:
            return
        
        if i < 0 or j < 0 or i >= size or j >= size:
            return

        if (i==size-1 and j==size-1 and array[i][j]==1):
            status = True
            return

        if(array[i][j]!=1):
            return
        
        if (array[i][j]==1):
            array[i][j]=2
            if i+1<size:
                checker(array,i+1,j)
            if i-1>=0:
                checker(array,i-1,j)
            if j+1<size:
                checker(array,i,j+1)
            if j-1>=0:
                checker(array,i,j-1)
    checker(arr,0,0)
    return status
arr=[[1,0,0,0],[1,1,0,0],[1,1,1,1],[0,0,1,0]]
size=4
print(maze(arr,4))
        
    
"""global status
status = False
def maze(arr,size):
       
    def checker(array,i,j):
        if i < 0 or j < 0 or i >= size or j >= size:
            return

        
        
        if (i==size-1 and j==size-1 and arr[i][j]==1):
            return True

        if(array[i][j]!=1):
            return
        
        if (array[i][j]==1):
            array[i][j]=2
            return checker(array,i+1,j) or checker(array,i-1,j) or checker(array,i,j+1) or checker(array,i,j-1)
    return checker(arr,0,0)
    
arr=[[1,0,0,0],[1,1,0,0],[1,1,1,1],[0,0,1,0]]
size=4
print(maze(arr,4))
"""        
    
