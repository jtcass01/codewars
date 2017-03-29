public class DnaStrand {

  public static String makeComplement(String dna) {

    String result = "";

  

    for(char letter : dna.toCharArray()){

      if(letter == 'A'){

        result += "T";

      } else if (letter == 'T') {

        result += "A";

      } else if (letter == 'G') {

        result += "C";

      } else if (letter == 'C') {

        result += "G";

      }

    }

    

    return result;

  }

}

