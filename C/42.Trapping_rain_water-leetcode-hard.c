int trap(int* height, int heightSize) {
    int left = 0, right = heightSize - 1;
    int leftMax = 0, rightMax = 0;
    int water = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax)
                leftMax = height[left];
            else
                water += leftMax - height[left];
            left++;
        } else {
            if (height[right] >= rightMax)
                rightMax = height[right];
            else
                water += rightMax - height[right];
            right--;
        }
    }

    return water;



    // int left =0,right=heightSize-1;
    // int max=0;
    // int leftval=height[left];
    // int rightval=height[right];
    // while(left<right){
    //     if(max<((leftval>rightval?rightval:leftval)*(right-left-1))){
    //         max=(leftval>rightval?rightval:leftval)*(right-left-1);
    //     }
    //     if(leftval>rightval){
    //         right--;
    //         rightval=height[right];
    //     }
    //     else{
    //         left++;
    //         leftval=height[left];
    //     }
    // }
    // return max;

}
