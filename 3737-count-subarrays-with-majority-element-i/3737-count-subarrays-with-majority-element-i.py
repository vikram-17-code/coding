class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        result = 0
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+(1 if nums[i]==target else 0)
        
        for i in range(n):
            for j in range(i,n):
                length = j-i+1
                count = prefix[j+1] - prefix[i]

                if (count>length/2):
                    result+=1
        return result