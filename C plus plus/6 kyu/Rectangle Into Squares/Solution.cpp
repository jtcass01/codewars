#include <vector>

using namespace std;

void printVector(const vector<int> &);
string intToString(const int &);

class SqInRect
{
  public:
  static vector<int> sqInRect(int lng, int wdth);
};


vector<int> SqInRect::sqInRect(int lng, int wdth) {
  vector<int> result;
  int longSide = 0, shortSide = 0, difference = 0, multiplicity = 0;
  
  if(lng == wdth){
    return result;
  } else if(lng > wdth){
    longSide = lng;
    shortSide = wdth;
  } else {
    longSide = wdth;
    shortSide = lng;
  }

  difference = shortSide;
  multiplicity = longSide / difference;
  
  for(unsigned int multiplicity_i = 0; multiplicity_i < multiplicity; multiplicity_i++){
    result.push_back(difference);
  }
  
  while(1){
    difference = longSide - (shortSide*multiplicity);

    if(difference == 0){
      break;
    }
    
    multiplicity = shortSide / difference;
    
    if(difference > shortSide){
      shortSide *= multiplicity;
      difference = longSide - shortSide;
    }

    for(unsigned int multiplicity_i = 0; multiplicity_i < multiplicity; multiplicity_i++){
      result.push_back(difference);
    }
    
    longSide = shortSide;
    shortSide = difference;

    printVector(result);
  }

  printVector(result);
  return result;
}

void printVector(const vector<int> &arr){
  string result = "<";
  
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    if(arr_i < arr.size()-1){
      result += intToString(arr[arr_i]) + ",";
    } else {
      result += intToString(arr[arr_i]) + ">";
    }
  }
  
  cout << result << endl;
}

string intToString(const int &val){
  return to_string(val);
}

