class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        # if(len(arr)==1):
        #     return [1]
        # elif(len(arr)==0):
        #     return []
        # ranks=[]
        # arrset = set(arr)
        # for i in range(len(arr)):
        #     counter = 1

        #     for j in arrset:
        #         if (arr[i]>j):
        #             counter +=1
        #     ranks.append(counter)
        # return ranks

        ranks ={}

        for i,num in enumerate(sorted(set(arr)),1):
            ranks[num]=i

        return [ranks[num] for num in arr]