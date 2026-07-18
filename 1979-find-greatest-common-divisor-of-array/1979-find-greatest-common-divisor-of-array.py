class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)
        for i in range(s,1,-1):
            if (s%i==0 and l%i==0):
                return i
        return 1