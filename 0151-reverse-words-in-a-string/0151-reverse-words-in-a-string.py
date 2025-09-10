class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        return (" ".join(list1[::-1]))