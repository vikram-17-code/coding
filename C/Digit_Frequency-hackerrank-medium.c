#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct freq{
    int num;
    int count;
};

int main() {
    struct freq times[10];
    char str1[1000];
    scanf("%s",str1);
    int n = strlen(str1);
    for(int i = 0;i<10;i++){
        times[i].num=i;
        times[i].count=0;
        
    }
    for(int i=0;i<n;i++){
        if(str1[i]=='0'){
            times[0].count+=1;
        }
        else if(str1[i]=='1'){
            times[1].count+=1;
        }
        else if(str1[i]=='2'){
            times[2].count+=1;
        }
        else if(str1[i]=='3'){
            times[3].count+=1;
        }
        else if(str1[i]=='4'){
            times[4].count+=1;
        }
        else if(str1[i]=='5'){
            times[5].count+=1;
        }
        else if(str1[i]=='6'){
            times[6].count+=1;
        }
        else if(str1[i]=='7'){
            times[7].count+=1;
        }
        else if(str1[i]=='8'){
            times[8].count+=1;
        }
        else if(str1[i]=='9'){
            times[9].count+=1;
        }
        
    }
    for(int i =0;i<10;i++){
        printf("%d ",times[i].count);
    }

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
