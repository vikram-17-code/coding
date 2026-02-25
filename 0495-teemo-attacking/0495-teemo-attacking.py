class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned =0
        for i in range(len(timeSeries)-1):
            if((timeSeries[i+1]-timeSeries[i])<duration):
               poisoned+=timeSeries[i+1]-timeSeries[i]
            else:
                poisoned+=duration
        return poisoned+duration
