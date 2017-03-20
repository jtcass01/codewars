#include <string>
#include <cmath>

using namespace std;

int charToInt(char);
bool sumOfCubesTest(string);
string reverse(string);

class RevRot
{
public:
    static string revRot(const string &strng, unsigned int sz);
};

string RevRot::revRot(const string &strng, unsigned int sz){
  string result = "", segment = "";
  
  if(sz == 0 || strng.compare("") == 0){
    return "";
  }

  for(unsigned int i = 0; i < strng.size(); i+= sz){
    segment = "";
    for(unsigned int j = i; j < i+sz && j < strng.size(); j++){
      segment += strng.at(j);
    }

    if(segment.size() == sz){
      if(sumOfCubesTest(segment)){
        result += reverse(segment);
      } else {
        if(segment.size() == sz){
          result += segment.substr(1,sz-1);
          result += segment.at(0);
        }
      }
    }
  }
  
  return result;
}

bool sumOfCubesTest(string integer){
  int sum = 0, currentInt = 0;
  
  for(unsigned int integer_i = 0; integer_i < integer.size(); integer_i++){
    currentInt = charToInt(integer.at(integer_i));
    sum += pow(currentInt, 3);
  }
  
  if(sum%2 == 0){
    return true;
  } else {
    return false;
  }
}

int charToInt(char c){
  return c - '0';
}

string reverse(string integer){
  string newString = "";
  
  for(unsigned int i = integer.size(); i > 0; i--){
    cout << i-1 << endl;
    newString += integer.at(i-1);
  }

  return newString;
}
