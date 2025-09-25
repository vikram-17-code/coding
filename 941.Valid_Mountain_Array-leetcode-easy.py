class Solution:
    def validMountainArray(self, li: List[int]) -> bool:
        if(len(li)==0 or len(li)==1 ):
            return False
    
        if(li[0]>=li[1]):
            return False

        found=False
        for i in range(1,len(li)-1):
            if(not found):
                if(li[i]==li[i+1]):
                    return False
                if(li[i]>li[i+1]):
                    found=True
                
            if(found):    
                if(li[i]==li[i+1]):
                    return False
                if(li[i]<li[i+1]):
                    found=False
                    break   
        return found
