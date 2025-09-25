int maxProfit(int* prices, int pricesSize) {
    int max=0;
    int minprice=prices[0];
    for(int i =1;i<pricesSize;i++){
        if (prices[i]<minprice){
            minprice=prices[i];
        }
        else if(prices[i] - minprice>max){
            max = prices[i] - minprice;

        }
    }
    return max;
}
