#include <string>
#include <cmath>

using namespace std;

class DigPow
{
public:
  static int digPow(int n, int p);
};

int DigPow::digPow(int n, int p){
  string n_string = to_string(n);
  int total = 0, currentInt = 0;
  
  for(unsigned int i=0; i < (n_string.size()); i++){
    char currentChar = n_string.at(i);
    currentInt = currentChar - '0';
    total += pow(currentInt, i+p);
  }
  
  if(total%n == 0){
    return total/n;
  } else{
    return -1;
  }
}
