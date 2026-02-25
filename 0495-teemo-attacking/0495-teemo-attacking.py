class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        arr = list(timeSeries)
        poisoned =0
        for i in range(len(timeSeries)):
            
            if (i+1 >= len(timeSeries)):
                poisoned+=duration
            else:
                if((arr[i+1]-arr[i])<duration):
                   poisoned+=arr[i+1]-arr[i]
                else:
                    poisoned+=duration
        return poisoned
