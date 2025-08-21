class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        x = re.sub("\W|_", "", s)
        return ( x==x[::-1])