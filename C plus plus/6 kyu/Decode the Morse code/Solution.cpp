using namespace std;

std::string decodeMorse(std::string morseCode) {
    string decoded = "", letter = "";
    int spaceCount = 0;
    bool start = false;
    
    for( unsigned int morseCode_i = 0; morseCode_i < morseCode.size(); morseCode_i++){
      string current = "";
      current += morseCode[morseCode_i];
      
      if(!start && current.compare(" ") == 0){
        ;
      } else if(!start){
        cout << "start found" << endl;
        start = true;
        letter += morseCode[morseCode_i];
      } else if(current.compare(" ") == 0){
        spaceCount++;
      } else if(spaceCount > 0){
        if(spaceCount == 1){
          decoded += MORSE_CODE[letter];
        } else {
          decoded += MORSE_CODE[letter];
          decoded += " ";
        }
        spaceCount = 0;
        letter = morseCode[morseCode_i];
      } else {
        letter += morseCode[morseCode_i];
      }
  
      if(morseCode_i == morseCode.size()-1){
        decoded += MORSE_CODE[letter];
      }
    }

  return decoded;
}
