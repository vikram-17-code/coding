int comp(const void *a,const void *b){
    return((*(int*)a)-(*(int*)b));
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
    double result=0;
    int newSize=nums1Size+nums2Size;
    int Newarr[newSize];
    for (int i =0;i<nums1Size;i++){
        Newarr[i]=nums1[i];
    }
    for(int i =nums1Size, j=0;i<(nums1Size+nums2Size);i++,j++){
        Newarr[i]=nums2[j];
    }
    qsort(Newarr,newSize,sizeof(int),comp);
    for(int i =0;i<newSize;i++){
        printf("%d",Newarr[i]);
    }
    if(newSize%2==0){

        int mid=newSize/2;
        result =((float)(Newarr[mid]+Newarr[mid-1])/2);
        return result;
    }
    else if(newSize%2==1){

        int mid=newSize/2;
        result =Newarr[mid];
        return result;
    }
    return result;
}
