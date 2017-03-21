#include <string>

using namespace std;

int charToInt(const char &c);
string intToString(const int &integer);

class PlayPass
{
  public:
  static std::string playPass(const std::string &s, int n);
  static string shiftLetters(const string &s, int n);
  static string complimentDigits(const string &s);
  static string bounceCase(const string &s);
  static string reverse(const string &s);
};

string PlayPass::playPass(const string &s, int n){
  cout << "_" << endl;
  
  cout << "Initial: " << s << " with n value of " << n << endl;

  string result = shiftLetters(s, n);
  result = complimentDigits(result);
  result = bounceCase(result);
  result = reverse(result);

  return result;
}

string PlayPass::shiftLetters(const string &s, int n){
  string result = "";
  
  for(unsigned int s_i = 0; s_i < s.size(); s_i++){
    if(isalpha(s[s_i])){
      if(s[s_i]+n > 90 && s[s_i] <= 90){
        result += char(s[s_i]+n+6);
      } else if(s[s_i]+n > 122){
        result += char(s[s_i]+n-58);
      } else {
        result += char(s[s_i]+n);
      }
    } else {
      result += s[s_i];
    }
  }
  
  return result;
}

string PlayPass::complimentDigits(const string &s){
  string result = "";
  
  for(unsigned int s_i = 0; s_i < s.size(); s_i++){
    if(isdigit(s[s_i])){
      result += intToString(9-charToInt(s[s_i]));
    } else {
      result += s[s_i];
    }
  }
  
  return result;
}

string PlayPass::bounceCase(const string &s){
  string result = "";
  
  for(unsigned int s_i = 0; s_i < s.size(); s_i++){
    if(isalpha(s[s_i])){
      if(s_i%2==0){ //even, upper
        result += toupper(s[s_i]);
      } else {  //odd, lower
        result += tolower(s[s_i]);
      }
    } else {
      result += s[s_i];
    }
  }
  
  return result;
}

string PlayPass::reverse(const string &s){
  string result = "";
  
  for(unsigned int s_i = 0; s_i < s.size(); s_i++){
    result = s[s_i] + result;
  }
  
  return result;
}


int charToInt(const char &c){
  return c - '0';
}

string intToString(const int &integer){
  return to_string(integer);
}
