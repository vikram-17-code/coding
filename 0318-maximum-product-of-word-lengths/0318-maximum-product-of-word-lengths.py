class Solution:
    def maxProduct(self, words: List[str]) -> int:
        val = 0
        sets = [set(word) for word in words]

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if sets[i].isdisjoint(sets[j]):
                    val = max(val, len(words[i]) * len(words[j]))

        return val