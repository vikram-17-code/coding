class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict1={}
        result=[]
        index=0
        key=key.replace(" ","")
        for char in key:
            if char not in dict1:
                dict1[char] = chr(97 + index)
                index += 1

        for i in message:
            if i == " ":
                result.append(" ")
            else:
                result.append(dict1[i])
        return "".join(result)

