class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balon"

        dict1 = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for c in text:
            if c in word:
                dict1[c]+=1

        return min(dict1["b"],dict1["a"],dict1["l"]//2,dict1["o"]//2,dict1["n"],)


