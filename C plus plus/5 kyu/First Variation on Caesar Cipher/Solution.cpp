#include <cmath>

using namespace std;

void printVector(const vector<string> &);

class CaesarCipher
{
  public:
    static std::vector<std::string> movingShift(const std::string &str, int shift);
    static std::string demovingShift(std::vector<std::string> &strArr, int shift);
    static int calculateMessageLengths(const string &);
    static char shiftLetter(const char &, int);
};

vector<string> CaesarCipher::movingShift(const string &str, int shift){
  string shiftedStr = "", message = "";
  vector<string> result;

  for(unsigned int str_i = 0; str_i < str.size(); str_i++){
    if(isalpha(str[str_i])){
      shiftedStr += shiftLetter(str[str_i], shift+str_i);
    } else {
      shiftedStr += str[str_i];
    }
  }
  
  int messageLengths = calculateMessageLengths(str);
  
  for(unsigned int line = 0; line < 4; line++){
    for(unsigned int message_i = 0; message_i < messageLengths; message_i++){
      message += shiftedStr[line*messageLengths+message_i];
    }
    result.push_back(message);
    message = "";
  }
  
  if(str.size() - messageLengths*4 > 0){
    for(unsigned int message_i = 0; message_i < str.size() - messageLengths*4; message_i++){
      message += shiftedStr[4*messageLengths+message_i];
    }
    result.push_back(message);
  } else {
    result.push_back("");
  }

  printVector(result);
  
  return result;
}

string CaesarCipher::demovingShift(vector<string> &strArr, int shift){
  string result = "";
  
  for(unsigned int strArr_i = 0; strArr_i < strArr.size(); strArr_i++){
    for(unsigned int message_i = 0; message_i < strArr[strArr_i].size(); message_i++){
      if(isalpha(strArr[strArr_i][message_i])){
        int currentShift = shift;
        currentShift += strArr[0].size()*strArr_i;
        currentShift += message_i;
        currentShift *= -1;
        result += shiftLetter(strArr[strArr_i][message_i], currentShift);
      } else {
        result += strArr[strArr_i][message_i];
      }
    }
  }
  
  return result;
}

int CaesarCipher::calculateMessageLengths(const string &str){
   return ceil(double(str.size()) / double(5));
}

char CaesarCipher::shiftLetter(const char &c, int shift){
  if(shift >= 0){
    shift %= 26;
  } else {
    shift %= -26;
  }

  if(isupper(c)){
    if(c+shift > 90){
      return char(c+shift-26);
    } else if (c+shift < 65) {
      return char(c+shift+26);
    } else {
      return char(c+shift);
    }
  } else {
    if(c+shift > 122){
      return char(c+shift-26);
    } else if (c+shift < 97) {
      return char(c+shift+26);
    } else {
      return char(c+shift);
    }
  }
}

void printVector(const vector<string> &arr){
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    cout << "|" << arr[arr_i] << "|" << endl;
  }
}
