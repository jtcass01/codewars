public class BouncingBall {
	
public static int bouncingBall(double h, double bounce, double window) {
    int result = 0;
    
    if(bounce >= 1 || bounce <= 0 || h < window){
      return -1;
    }
    
    while(h > window){
      h *= bounce; //Find new height
      if(h > window){
        result += 2; //Count ball going back up.
      } else {
        result += 1; //Count ball going down.
      }
    }

    if(result == 0){
      return -1;
    } else {
      return result;
    }
}

}
