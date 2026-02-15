from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter=Counter(s)
        for a,i in s_counter.items():
            if (i==1):
                    for j,k in enumerate(s):
                        if k==a:
                            return j
                
        return -1