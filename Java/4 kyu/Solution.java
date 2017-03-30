import java.util.*;

public class CarMileage {

  public static int isInteresting(int number, int[] awesomePhrases) {
    if(number < 98){
      return 0;
    }
  
    for(int number_i = number; number_i < number+3; number_i++){
      if(number_i >= 100) {
        System.out.println(number_i);
  
        if(followedByZeroes(number_i) || sameNumber(number_i) || sequentialInc(number_i) || sequentialDec(number_i) || palindrome(number_i)){
          if(number_i == number){
            return 2;
          } else {
            return 1;
          }
        }
        
        for(int value : awesomePhrases){
          if(value == number_i){
            if(number_i == number){
              return 2;
            } else {
              return 1;
            }
          }
        }
      }
    }
    
    return 0;
  }
  
  public static boolean followedByZeroes(int num){
    Integer number = new Integer(num);
    boolean firstNumber = true;
    
    for(char character : number.toString().toCharArray()){
      if(!firstNumber && character != '0'){
        return false;
      } else if (Character.isDigit(character) && character != '0' && firstNumber) {
        firstNumber = false;
      }
    }
    
    return true;
  }
  
  public static boolean sameNumber(int num){
    Integer number = new Integer(num);
    boolean firstNumber = true;
    char firstNum = '\0';
    
    for(char character : number.toString().toCharArray()){
      if(Character.isDigit(character) && firstNumber){
        firstNumber = false;
        firstNum = character;
      } else {
        if(character != firstNum){
          return false;
        }
      }
    }
    
    return true;    
  }
  
  public static boolean sequentialInc(int num){
    Integer number = new Integer(num);
    boolean firstNumber = true;
    Integer last = new Integer(0);
    Integer next = new Integer(0);
    
    for(char character : number.toString().toCharArray()){
      if(firstNumber){
        last = Character.getNumericValue(character);
        if(last == 9){
          next = 0;
        } else {
          next = last +1 ;
        }
        firstNumber = false;
      } else {
        if(next == Character.getNumericValue(character)){
          last = Character.getNumericValue(character);
          if(last == 9){
            next = 0;
          } else {
            next = last +1 ;
          }
        } else {
          return false;
        }
      }
    }
    
    return true;
  }
  
  public static boolean sequentialDec(int num){
    Integer number = new Integer(num);
    boolean firstNumber = true;
    Integer last = new Integer(0);
    Integer next = new Integer(0);

    for(char character : number.toString().toCharArray()){
      if(firstNumber){
        last = Character.getNumericValue(character);
        if(last == 0){
          next = 9;
        } else {
          next = last - 1 ;
        }
        firstNumber = false;
      } else {
        if(next == Character.getNumericValue(character)){
          last = Character.getNumericValue(character);
          if(last == 0){
            next = 9;
          } else {
            next = last - 1 ;
          }
        } else {
          return false;
        }
      }
    }
    
    return true;
  }
  
  public static boolean palindrome(int num){
    Integer number = new Integer(num);
    String numStr = number.toString();
    
    for(int num_i = 0; num_i < numStr.length()/2; num_i++){
      if(numStr.charAt(num_i) != numStr.charAt(numStr.length()-1-num_i)){
        return false;
      }
    }
    
    return true;
  }
}
