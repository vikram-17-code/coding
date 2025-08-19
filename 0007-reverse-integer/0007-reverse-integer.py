class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            result=str(abs(x))

            result=result[::-1]
            result=-(int(result))
            if (result>-(2**31) and result<((2**31)-1)):
                return result
            return 0
        else:
            result=str(x)
            result=int(result[::-1])
            if (result>-(2**31) and result<((2**31)-1)):
                return result
            return 0
        
        
        