public class Solution {
  public int solution(int number) {
    int result = 0;
  
    for(int i = 0; i < number; i++){
      if(i % 3 == 0){
        result += i;
      } else if (i % 5 == 0){
        result += i;
      }
    }
    
    return result;
  }
}
