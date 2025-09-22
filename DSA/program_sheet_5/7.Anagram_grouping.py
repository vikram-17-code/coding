strs=list(map(str,input().split()))
dict1={}
result=[]
for i in strs:
    key =''.join(sorted(i))
    if key not in dict1:
        dict1[key]=[i]
    else:
        dict1[key].append(i)
    

result = list(dict1.values())


print(result)
            
        
