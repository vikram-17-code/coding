import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumd=[]
        pro_d=[]
        while(n>0):
            temp=n%10;
            sumd.append(temp)
            pro_d.append(temp)
            n=n//10;
        S_D=sum(sumd)
        P_d=math.prod(pro_d)
        return (P_d-S_D)
