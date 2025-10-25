#include<stdio.h>
#include<ctype.h>
#include<string.h>

void reverse(char *s,int start,int end){
    for(int i =0;i<end/2;i++){
        char *temp= s[start];
        s[start]=s[end];
        s[end]=*temp;
    }
}

void reverseeach(char *s){
    int i=0,j=0;
    int len=strlen(s)
    while(j<len){
        if(isspace(s[j])){
            reverse(s,i,j-1);
            i=j+1;
        }
        j++
        
    }
    
}

void removespace(char *s){
    char *s1 = s;
    int len=strlen(s)
    int j=0;
    int i=0;
    while(i<len){
        if(isspace(s[i])){
            s1[j++]=' ';
            while(isspace(s[i]))i++;
        }
        s1[j++]=s[i++];
    }
    if(s1[-1]==' '){
        s1[-1]='\0';
    }
}
void main(){
    char s[1000];
    fgets(s,sizeof(s),stdin);
    int len=strlrn(s);
    if(len>0 && s[len -1] == '\n'){
        s[len -1]='\0';
        len--;
    }
    while(len>0 && isspace((unsigned char)s[len - 1])){
        s[len -1] = '\0';
        len--;
    }
    remove
    

}

