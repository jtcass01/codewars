using namespace std;

void print(const vector<char> &);
void print(const vector<vector<char>> &);
bool valid_braces(string);
int findVectorIndex(const char &, const vector<vector<char>> &);

bool valid_braces(std::string str) {
  vector<char> stack;
  vector<vector<char>> braces;
  vector<char> bracesGroup;
  int vectorIndex;

  bracesGroup.push_back('('); bracesGroup.push_back(')'); braces.push_back(bracesGroup); bracesGroup.clear();
  bracesGroup.push_back('{'); bracesGroup.push_back('}'); braces.push_back(bracesGroup); bracesGroup.clear();
  bracesGroup.push_back('['); bracesGroup.push_back(']'); braces.push_back(bracesGroup); bracesGroup.clear();

  for(unsigned int str_i = 0; str_i < str.size(); str_i++){
    for(unsigned int openBraces_i = 0; openBraces_i < braces.size(); openBraces_i++){
      if(str[str_i] == braces[openBraces_i][0]){
        stack.insert(stack.begin(), str[str_i]);
      }
    }

    for(unsigned int closeBraces_i = 0; closeBraces_i < braces.size(); closeBraces_i++){
      if(str[str_i] == braces[closeBraces_i][1]){
        if(stack.size() > 0){
          vectorIndex = findVectorIndex(str[str_i], braces);
          if(braces[vectorIndex][0] == stack[0]){
            stack.erase(stack.begin());
          } else {
            return false;
          }
        } else {
          return false;
        }
      }
    }
  }

  if(stack.size() > 0){
    return false;
  } else {
    return true;
  }
}

void print(const vector<char> &arr){
  cout << "[";

  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    if(arr_i != arr.size()-1){
      cout << arr[arr_i] << ",";
    } else {
      cout << arr[arr_i] << "]" << endl;
    }
  }
}

void print(const vector<vector<char>> &arr){
  cout << "[[";

  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    for(unsigned int arr_j = 0; arr_j < (arr[arr_i]).size(); arr_j++){
      if(arr_j != arr[arr_i].size()-1){
        cout << '\'' << arr[arr_i][arr_j] << '\'' << ",";
      } else {
        cout << "\'" << arr[arr_i][arr_j] << "\'" << "]";
      }
    }
    if(arr_i != arr.size()-1){
      cout << ",[";
    } else {
      cout << "]" << endl;
    }
  }
}

int findVectorIndex(const char &c, const vector<vector<char>> &arr){
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    for(unsigned int arr_j = 0; arr_j < arr[0].size(); arr_j++){
      if(arr[arr_i][arr_j] == c){
        return arr_i;
      }
    }
  }
  return 404;
}
