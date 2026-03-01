class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor^=i
        diff = xor & -xor

        a=0
        b=0

        for i in nums:
            if(i&diff):
                a^=i
            else:
                b^=i

        return [a,b]
        