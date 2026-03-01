class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if (dict1.get(i,0)):
                dict1[i]+=1
            else:
                dict1[i]=1
        
        for i,j in dict1.items():
            if j==1:
                return i