class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = len(s)
        result=0
        skip=False
        for i in range(n):
            if skip:
                skip = False
                continue
            if (i<n-1) and roman[s[i+1]]>roman[s[i]]:
                result += (roman[s[i+1]]-roman[s[i]])
                skip=True
                print(result , i)
            else:
                result += roman[s[i]]
                print(result,i)
        return result