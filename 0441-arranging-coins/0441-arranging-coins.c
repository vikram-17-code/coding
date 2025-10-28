int arrangeCoins(int n) {
    /*int result;
    for(int i=1;i<=n;i++){
        int sum =0;
        for(int j =1;j<=i;j++){
            sum+=j;
        }
        if (sum>=n){
            if (sum==n){
                result= i;
                break;
            }
            else{
                result= i-1;
                break;
            }
        }
    }
    return result;*/
    int i = 1;
    while ((long long)i * (i + 1) / 2 <= n) {
        i++;
    }
    return i - 1;
}