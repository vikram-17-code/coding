class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs)
        result = [0]*(n+1)
        candy=0
        for i in costs:
            result[i]+=1

        for i,j in enumerate(result):
            while(j>0):
                if(i<=coins):
                    candy+=1
                    coins-=i
                    j-=1
                else:
                    break
            if(i>coins):
                break
        return candy