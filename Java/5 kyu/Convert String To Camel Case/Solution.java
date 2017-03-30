import java.lang.StringBuilder;
import java.util.*;

class Solution{

  static String toCamelCase(String s){
    boolean space = false;
    String str = "";

    for(char character : s.toCharArray()){
      if(Character.isLetter(character)){
        if(space == true){
          str += Character.toUpperCase(character);
          space = false;
        } else {
          str += character;
        }
      } else {
        space = true;
      }
    }

    return str;
  }
}
