class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if(len(pattern)!=len(s)):
            return False
        sd={}
        td={}
        for i,j in zip(pattern,s) :
            if i in sd:
                if sd[i]!=j:
                    return False

            if j in td:
                if td[j]!=i:
                    return False
            
            if i not in sd:
                sd[i]=j
            if j not in td:
                td[j]=i
        
        return True