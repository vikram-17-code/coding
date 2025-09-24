class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            num=list(str(num))
            num=sum([int(x) for x in num])
            
        return num    
