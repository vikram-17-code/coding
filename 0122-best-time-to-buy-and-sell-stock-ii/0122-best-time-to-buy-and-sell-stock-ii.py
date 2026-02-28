class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        best=0
        for i in prices:
            if(i<mini):
                mini=i
            if(mini<i):
                best += (i-mini)
                mini = i
        return best