class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        result =[]
        for i in words:
            j = set(i.lower())
            if j<=first:
                result.append(i)
            if j<=second:
                result.append(i)
            if j<=third:
                result.append(i)
        
        return result
           