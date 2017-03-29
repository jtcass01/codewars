import java.util.*;

public class FindOutlier{

  static int find(int[] integers){

    ArrayList<Integer> odds = new ArrayList<Integer>();

    ArrayList<Integer> evens = new ArrayList<Integer>();

  

    for(int num : integers){

      if(num % 2 == 0){

        if(odds.size() > 1) {

          return num;

        } else {

          if(evens.size() < 2){

            evens.add(num);

          }

        }

      } else {

        if(evens.size() > 1){

          return num;

        } else {

          if(odds.size() < 2){

            odds.add(num);

          }

        }

      }

      

      if(evens.size() > 0 && odds.size() > 1){

        return evens.get(0);

      }  else if (evens.size() > 1 && odds.size() > 0){

        return odds.get(0);

      }

    }

    return 0;

}}
