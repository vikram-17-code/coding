#include<stdio.h>
void ranker(int arr[],int n){
    int rank[n];
    for(int i=0; i<n;i++){
        rank[i]=1;
        for(int j=0;j<n;j++){
            if(arr[i]>arr[j]){
                rank[i]++;
            }
        }
    }
    for(int i =0;i<n;i++){
        printf("%d ",rank[i]);
    }
}
void main(){
    int n;
    printf("Enter size:");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    ranker(arr,n);
}
