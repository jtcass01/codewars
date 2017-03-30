import java.lang.*;

public class Tortoise {
    public static int[] race(int v1, int v2, int g) {
        int relativeSpeed = v2 - v1;
        double time = 0;
        int hours = 0, minutes = 0, seconds = 0;
        
        System.out.println("v1: " + v1 + "\tv2: " + v2 + "\tg: " + g);
        System.out.println("RelativeSpeed: " + relativeSpeed);
        
        if(relativeSpeed <= 0 && g != 0){
          return null;
        } else {
          time = (double)(g) * ((double)(1)/(double)(relativeSpeed));
          System.out.println("Initial time: " + time);
          hours = (int)(Math.floor(time));
          time %= 1;
          time *= 60;
          minutes = (int)(Math.floor(time));
          time %= 1;
          time *= 60;
          seconds = (int)(Math.floor(time));
          System.out.println("Hours: " + hours + "\tMinutes: " + minutes + "\tSeconds: " + seconds);
          return new int[]{hours, minutes, seconds};
        }
    }
}
