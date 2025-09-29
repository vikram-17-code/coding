class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i=1
        arr=[[0]*n for i in range(n)]
        top,bottom=0,n-1
        left,right=0,n-1
        while(top<=bottom and left<=right):
            
            for j in range(left,right+1):
                arr[top][j]=i
                i+=1
            top+=1

            for j in range(top,bottom+1):
                arr[j][right]=i
                i+=1
            right-=1

            if(left<=right):
                
                for j in range(right,left-1,-1):
                    arr[bottom][j]=i
                    i+=1
                bottom-=1
            
            if(top<=bottom):
                
                for j in range(bottom,top-1,-1):
                    arr[j][left]=i
                    i+=1
                left+=1

        return arr
