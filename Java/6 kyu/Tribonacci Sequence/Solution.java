public class Xbonacci {

  public double[] tribonacci(double[] s, int n) {
    double[] result = new double[n];
    int difference = n - s.length;
    
    if(n < s.length && n != 0){
      for(int s_i = 0; s_i < n; s_i++){
        result[s_i] = s[s_i];
      }
      return result;
    } else if (n == 0){
      return new double[]{};
    } else {
      for(int result_i = 0; result_i < result.length; result_i++){
        if(result_i < s.length){
          result[result_i] = s[result_i];
        } else {
          result[result_i] = result[result_i-3] + result[result_i-2] + result[result_i-1];
        }
      }
    }      
      
    return result;
  }
  
  public static void printArray(double[] arr){
    System.out.print("[");
    
    for(int arr_i = 0; arr_i < arr.length; arr_i++){
      if(arr_i != arr.length-1){
        System.out.print(arr[arr_i] + ", ");
      } else {
        System.out.println(arr[arr_i] + "]");
      }
    }
  }
}
