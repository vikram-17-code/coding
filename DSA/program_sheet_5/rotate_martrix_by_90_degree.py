rows=int(input("rows:"))

arr=[]
for i in range(rows):
    row=list(map(int,input("enter values for the row:").split()))
    if len(row)!=rows:
        print("invalid number of columns:")
        break
    arr.append(row)
    
for i in range(rows):
    for j in range(i+1,rows):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
for k,i in enumerate(arr):
    #temp=[]
    i.reverse()
    #for j in i[::-1]:
    #   temp.append(j)
    #arr[k]=temp
        

print(arr)
