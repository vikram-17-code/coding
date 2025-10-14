class Solution:
    def removeDuplicates(self, s: str) -> str:
        news=[]
        for i in range(len(s)):
            if news and news[-1]==s[i]:
                news.pop()
            else:
                news.append(s[i])
        return "".join(news)
