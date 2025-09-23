struct count{
    int number;
    int times;
};
int mostFrequentEven(int* nums, int numsSize) {
    struct count arr[numsSize];
    int k=0;
    for(int i =0;i<numsSize;i++){

        if(nums[i]%2==1){
            continue;
        }
        int found =0;
        for(int j =0;j<k;j++){
            if(nums[i]==arr[j].number){
                arr[j].times++;
                found=1;
                break;
            }
        }
        if(!found){
            arr[k].number=nums[i];
            arr[k].times=1;
            k++;
        }
    }
    if(k==0){
        return -1;
    }
    int number;
    int max=0;
    for(int i =0;i<k;i++){
        if(max<arr[i].times){
            number=arr[i].number;
            max=arr[i].times;
        }
        else if(max==arr[i].times){
            if(number>arr[i].number){
                number=arr[i].number;
            }
        }
    }
    return number;
}