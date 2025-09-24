bool isPowerOfTwo(int n) {
    return n>0 && (n &(n-1)) == 0;
    //for(int i=0;i<(n/2)+1;i++){
    //    if(pow(2,i)==n){
    //        return true;
    //   }
    //}
    //return false;
}
