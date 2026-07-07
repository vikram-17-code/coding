class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        longest = 0

        for num in nums:
            if num in dic:
                continue

            left = dic.get(num - 1, 0)
            right = dic.get(num + 1, 0)

            length = left + right + 1

            dic[num] = length

            # Update only the boundaries
            dic[num - left] = length
            dic[num + right] = length

            longest = max(longest, length)

        return longest