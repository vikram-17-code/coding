#include<stdio.h>
#include<stdlib.h>
void main(){
    while(1){
        int qs,correct=0;
        printf("enter value:");
        scanf("%d",&qs);
        int *key=(int*)malloc(qs*sizeof(int));
        printf("enter the keys in a single line:");
        for(int i =0 ;i<qs;i++){
            scanf("%d",&key[i]);
        }
        int ans;
        printf("enter answers:");
        for(int i =0 ;i<qs;i++){

            scanf("%d",&ans);
            if(key[i]==ans)
                correct++;
            }
        free(key);
        printf("mark=%d\n",correct);
        printf("percentage=%.2f%%\n",((float)correct/(float)qs)*100);
        printf("do you want to continue:(y/n)");
        char ch;
        scanf(" %c",&ch);
        if(ch!='y')
                break;
    }
}
