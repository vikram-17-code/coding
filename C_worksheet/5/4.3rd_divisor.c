#include<stdio.h>
void main(){
    int m,n,k,result=0;
    printf("enter values for m,n,k:");
    scanf("%d %d %d",&m,&n,&k);
    int counter=0;
    int max=0;
    int i;
    if (m<n)
       max=m;
    else
       max=n;
    if((max/2)<k)
        i = max/2;
    else
        i=k;
    printf("%d",i);

    for(;i>0;i--){
        if ((n%i==0) && (m%i==0)){
            counter+=1;
            if (counter==3){
                result=i;
            }
        }
    }
    printf("result:%d",result);
}
