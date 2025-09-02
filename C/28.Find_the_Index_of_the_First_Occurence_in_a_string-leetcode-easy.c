#include<string.h>
int strStr(char* haystack, char* needle) {
    char *result=strstr(haystack,needle);
    if (result != NULL){
        int index = result-haystack;
        return index;
    }
    else{
        return -1;
    }
    
}
