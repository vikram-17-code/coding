int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int i=1;
    for(int j=i;j<numsSize;j++){
        if(nums[j]!=nums[i-1]){
            nums[i]=nums[j];
            i++;
        }
    }
    return i;
}