#include<stdio.h>
#include<string.h>
int swapstat(char *a,char *b,int n,int n2){
    if(n!=n2){
        return 0;
        }
    int j=0;
    int swapped=0;
    for(int i = 0 ; i<n ; i++){
        if(a[i]!=b[i]){
            j=i;
            for(int k=i;k<n;k++){
                if((a[k]==b[j]) && (b[k]==a[j])){
                    char temp=a[k];
                    a[k]=a[j];
                    a[j]= temp;
                    swapped++;
                    printf("%s",a);
                    break;
                }
            }

        }
    if (swapped<2){
        for(int i=0;i<n;i++){
            if(a[i]!=b[i]){
                return 0;
            }

        }
        return 1;
    }
    return 0;

    }
}
void main(){
    char *a=malloc(100),*b=malloc(100);
    printf("enter 1st val");
    scanf("%s",a);
    printf("enter 2nd val");
    scanf("%s",b);
    int size1 = strlen(a);
    int size2 = strlen(b);
    printf("the string is %d",swapstat(a,b,size1,size2));




}
