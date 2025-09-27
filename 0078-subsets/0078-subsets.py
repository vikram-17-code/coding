class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if(len(nums)==0):
            return [[]]
        result=[]
        def backtracking(start,path):
            result.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()          
        backtracking(0,[])
        result=(result)
        return result

        
        