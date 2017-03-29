public class Kata {
  public static String createPhoneNumber(int[] numbers) {
    String result = "(";
    
    for(int numbers_i = 0; numbers_i < numbers.length; numbers_i++){
      result += numbers[numbers_i];
      
      if(numbers_i == 2){
        result += ") ";
      } else if (numbers_i == 5){
        result += "-";
      }
    }
    
    return result;
  }
}
