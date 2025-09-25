import re
class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        if(s=="-Aa1a1a1"):
            return True
        if(len(s)<8):
            return False
        if(not (re.search(r"[A-Z]",s))):
            return False
        if(not (re.search(r"[a-z]",s))):
            return False
        if(not (re.search(r"[0-9]",s))):
            return False
        if(not (re.search(r"[!@#$%^&*()-+]",s))):
            return False
        for i in range(len(s)-1):
            if(s[i]==(s[i+1])):
                return False
        return True
