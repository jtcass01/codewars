#include <string>
#include <cmath>

using namespace std;

vector<float> getNums(string, const string &);
void printNums(const vector<float> &);

class Rainfall
{
public:
    static double mean(std::string town, const std::string &strng);
    static double variance(std::string town, const std::string &strng);
};

double Rainfall::mean(string town, const string &strng){
  vector<float> nums = getNums(town, strng);
  float total = 0;

  for(int nums_i = 0; nums_i < nums.size(); nums_i++){
    total += nums[nums_i];
  }
  
  printNums(nums);

  if(nums.size() == 0){
    return -1;
  } else {
    return double(total/nums.size());
  }
}

double Rainfall::variance(string town, const string &strng){
  vector<float> nums = getNums(town, strng);
  double mean = Rainfall::mean(town, strng);
  double variance = 0;
  
  for(unsigned int nums_i = 0; nums_i < nums.size(); nums_i++){
    double currentVariance = mean-nums[nums_i];
    variance += currentVariance*currentVariance;
  }

  if(nums.size() == 0){
    return -1;
  } else {
    return variance / nums.size();
  }
}

void printNums(const vector<float> &arr){
  cout << "<";

  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    if(arr_i < arr.size()-1){
      cout << arr.at(arr_i) << ",";
    } else {
      cout << arr.at(arr_i);
    }
  }
  cout << ">" << endl;
}

vector<float> getNums(string town, const string &strng){
  string city = "", num = "";
  bool newCity = true, foundCity = false, newNumber = false;
  vector<float> nums;

  string test1 = "Rom", test2 = "Rome";

  for(int data_i = 0; data_i < strng.length(); data_i++){
    string current = string(1, strng.at(data_i));
    
    if(newCity){
      city += current;
    }

    if(current.compare(":") == 0){
      newCity = false;
      city = city.substr(0, city.size()-1);
      if(city.compare(town) == 0){
        foundCity = true;
      }
    } else if (current.compare("\n") == 0 && !foundCity) {
      newCity = true;
      city = "";
    } else if (city.compare(town) == 0 && city.size() == town.size()) {
    }
    
    if(foundCity){      
      if(current.compare(" ") == 0){
        newNumber = true;
      } else if(newNumber) {
        if(current.compare(",") == 0){
          nums.push_back(stof(num));
          num = "";
          newNumber = false;
        } else if (current.compare("\n") == 0) {
          nums.push_back(stof(num));
          newCity = true;
          foundCity = false;
          city = "";
          num = "";
        } else {
          num += current;
        }
      }

      if(data_i == strng.size()-1){
         nums.push_back(stof(num));
      }
    }
  }
    
  return nums;
}
