class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        
    
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
        for k,i in enumerate(arr):
            i.reverse()
        return arr