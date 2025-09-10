#include<stdio.h>
#include<stdlib.h>
void main(){
    int size;
    int swapA,swapB;
    printf("enter size:");
    scanf("%d",&size);
    int A[size][size];
    int AT[size][size];
    int B[size][size];
    int C[size][size];
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            scanf("%d",&A[i][j]);
        }
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            AT[i][j]=A[i][j];
        }
    }

    for(int i=0;i<size-1;i++){
        for(int j=i+1;j<size;j++){
            swapA=AT[j][i];
            swapB=AT[i][j];
            AT[i][j]=swapA;
            AT[j][i]=swapB;
        }
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            B[i][j]=(AT[i][j]+A[i][j])/2;
            C[i][j]=(A[i][j]-AT[i][j])/2;
        }
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            printf("%d ",A[i][j]);
        }
        printf("\n");
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            printf("%d ",B[i][j]);
        }
        printf("\n");
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            printf("%d ",C[i][j]);
        }
        printf("\n");
    }





}
