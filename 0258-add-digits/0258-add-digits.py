class Solution:
    def addDigits(self, num: int) -> int:
        if(num==0):
            return 0
        if((1+(num-1))%9==0):
            return 9  
        return (1+(num-1))%9    
