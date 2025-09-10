#include<stdio.h>
void main(){
    int n=0,i=0;
    printf("no of salesperson:");
    scanf("%d",&n);
    int arr[n];
    int min=0,total=0,max=0;
    int high,low;
    int one_time=1;
    for(;i<n;i++){
        printf("value:");
        scanf("%d",&arr[i]);
        total+=arr[i];
        if (one_time==1){
            min=arr[i];
            one_time=0;
            low=i+1;
        }
        if(max<arr[i]){
            max=arr[i];
            high=i+1;
        }
        if(min>arr[i]){
            min=arr[i];
            low=i+1;
        }

    }
    for(i=0;i<n;i++){
        printf("id:%d amount=%d\n",i+1,arr[i]);
    }
    int average=total/n;
    printf("average:%d\n",average);
    printf("saleperson %d had the highest sale with %d\n",high,max);
    printf("saleperson %d had the lowest sale with %d\n",low,min);
    int amount,exceed=0;
    printf("enter the amount:");
    scanf("%d",&amount);
    for (i =0;i<n;i++){
        if(arr[i]>=amount){
            printf("id:%d\n",i+1);
            exceed++;

        }
    }
    printf("no of sale people exceeding amount is %d",exceed);
}
