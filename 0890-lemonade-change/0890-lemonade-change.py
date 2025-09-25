class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict1={5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i]==5:
                dict1[5]+=1
                continue
            if bills[i]==10:
                if dict1[5]==0:
                    return False
                dict1[5]-=1
                dict1[10]+=1
                continue
            if bills[i]==20:
                if dict1[5]==0:
                    return False
                if (dict1[10]>0 and dict1[5]>0):
                    dict1[5]-=1    
                    dict1[10]-=1
                    dict1[20]+=1
                    continue
                if((dict1[5])>2):
                    dict1[5]-=3
                    dict1[20]+=1
                    continue
                return False
        return True
        