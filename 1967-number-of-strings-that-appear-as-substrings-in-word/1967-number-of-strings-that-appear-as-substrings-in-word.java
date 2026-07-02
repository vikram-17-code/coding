class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int result=0;
        for(String ch :patterns){
            if(word.contains(ch)){
                result+=1;
            }
        }
         return result;
    }
   
}