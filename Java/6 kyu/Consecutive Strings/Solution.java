class LongestConsec {
    
    public static String longestConsec(String[] strarr, int k) {
      String result = "", temp = "";
      int maxLength = 0;
      
      if(strarr.length < 1 || k==0 || k > strarr.length){
        return "";
      }
      
      for(int strarr_i = 0; strarr_i < k; strarr_i++){
        result += strarr[strarr_i];
      }
      
      maxLength = result.length();
    
      for(int strarr_i = 0; strarr_i < strarr.length-k+1; strarr_i++){
        for(int k_i = strarr_i; k_i < k+strarr_i; k_i++){
          temp += strarr[k_i];
        }
        if(temp.length() > maxLength){
          maxLength = temp.length();
          result = temp;
          temp = "";
        } else {
          temp = "";
        }
      }
      
      return result;
    }
    
    public static String printArray(String[] arr){
      String result = "[";
      
      for(String value : arr){
        result += value + ", ";
      }
      
      return result.substring(0, result.length()-2) + "]";
    }
}
