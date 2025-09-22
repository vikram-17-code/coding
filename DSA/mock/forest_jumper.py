stones=list(map(int,input().split()))
i=0
while(i<len(stones)):
    temp=i
    i+=stones[i];
    if i>=(len(stones)-1):
        print("True")
        break
    if temp==i:
        print("False")
        break
