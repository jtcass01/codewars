using namespace std;

class weight{
  protected:
    string num;
    int total;
  public:
    weight();
    weight(string);
    int findTotal(const string &);
    void setNumber(const string &);
    inline string getNumber(void){return num;}
    inline int getTotal(void){return total;}
    friend bool operator>(const weight &, const weight &);
    friend bool operator<(const weight &, const weight &);
    friend ostream& operator<<(ostream& os, weight wt){
      os << "_\nNumber: " << wt.getNumber() << endl << "Total: " << wt.getTotal();
      return os;
    }
    void operator=(const weight &old){
      num = old.num;
      total = old.total;
    }
};

class WeightSort
{
public:
    static std::string orderWeight(const std::string &strng);
    static vector<weight> sort(vector<weight>);
};


int charToInt(const char &);
void printWeightArray(vector<weight>);
string joinArray(vector<weight>);

weight::weight(){
  num = "";
  total = 0;
}

weight::weight(string number){
  num = number;
  total = findTotal(number);
}

int weight::findTotal(const string &str){
  int sum = 0;
  
  for(unsigned int str_i = 0; str_i < str.size(); str_i++){
    sum += charToInt(str[str_i]);
  }
  
  return sum;
}

void weight::setNumber(const string &str){
  num = str;
  total = findTotal(str);
}

bool operator>(const weight &w1, const weight &w2){
  if(w1.total == w2.total){
    return w1.num > w2.num;
  } else {
    return w1.total > w2.total;
  }
}

bool operator<(const weight &w1, const weight &w2){
  if(w1.total == w2.total){
    return w1.num < w2.num;
  } else {
    return w1.total < w2.total;
  }
}

string WeightSort::orderWeight(const string &strng){
  vector<weight> arr;
  weight current_weight;

  if(strng == ""){
    return strng;
  }

  string num = "", result = "";

  for(unsigned int i = 0; i < strng.size(); i++){
    if(isdigit(strng[i])){
      num += strng[i];
    } else {
      current_weight.setNumber(num);
      arr.push_back(current_weight);
      num = "";
    }
  }

  if(isdigit(num[0])){
    current_weight.setNumber(num);
    arr.push_back(current_weight);
  }


//  cout << "_____BEFORE _ SORT_____" << endl;
//  printWeightArray(arr);
  arr = sort(arr);
//  cout << "_____AFTER _ SORT_____" << endl;
//  printWeightArray(arr);
  
  return joinArray(arr);
}

vector<weight> WeightSort::sort(vector<weight> array){
  weight minWeight("0001"), temp("0001");
  int minLocation = 0;

  for(unsigned int array_i = 0; array_i < array.size(); array_i++){
    minWeight = array[array_i];
    minLocation = array_i;
    for(unsigned int array_j = array_i; array_j < array.size(); array_j++){
      if(array[array_j] < minWeight){
        minWeight = array[array_j];
        minLocation = array_j;
      }
    }
    temp = array[array_i];
    array[array_i] = minWeight;
    array[minLocation] = temp;
  }
  
  return array;
}

int charToInt(const char &c){
  return c - '0';
}

void printWeightArray(vector<weight> arr){
  cout << "===== Printing Weight Array =====" << endl;
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    cout <<  arr[arr_i] << endl;
  }
}

string joinArray(vector<weight> arr){
  string str = "";
  
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    str +=  arr[arr_i].getNumber() + " ";
  }
  
  return str.substr(0, str.size()-1);
}
