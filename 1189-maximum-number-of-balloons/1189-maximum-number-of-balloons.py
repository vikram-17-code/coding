class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balon"
        result = 0
        dict1 = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for c in text:
            if c in word:
                dict1[c]+=1

        while(True):
            if (dict1["b"]>0 and dict1["a"]>0 and dict1["l"]>1 and dict1["o"]>1 and dict1["n"]>0):
                dict1["b"]-=1
                dict1["a"]-=1
                dict1["l"]-=2
                dict1["o"]-=2
                dict1["n"]-=1
                result +=1
            else:
                break
        return result


