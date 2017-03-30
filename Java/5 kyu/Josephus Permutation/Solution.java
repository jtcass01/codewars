import java.util.*;

public class Josephus {
  public static <T> List<T> josephusPermutation(final List<T> items, final int k) {
    int items_i = 0;
    List<T> result = new ArrayList();
    
    while(items.size() > 0){
      if(items.size() > 0){
        items_i = incrementIndex(items_i, items.size(), k-1);
      }
      result.add(items.get(items_i));
      items.remove(items_i);
    }
    
    printList(result);
    return result;
  }
  
  public static int incrementIndex(int index, int max, int increment){
    
    for(int increment_i = 0; increment_i < increment; increment_i++){
      index++;
      if(index == max){
        index = 0;
      } else if(index > max) {
        index -= max;
      }
    }

    if(max == 1){
      return 0;
    } else {
      return index;
    }
  }
  
  public static void printList(List arr){
    System.out.print("[");
    
    for(int arr_i = 0; arr_i < arr.size(); arr_i++){
      if(arr_i != arr.size() -1){
        System.out.print(arr.get(arr_i) + ", ");
      } else {
        System.out.println(arr.get(arr_i) + "]");
      }
    }
  }
}
