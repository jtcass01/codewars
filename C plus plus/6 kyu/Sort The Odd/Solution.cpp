#include <vector>

using namespace std;

void printArray(const vector<int> &);
vector<int> sort(vector<int>);

class Kata
{
public:
    vector<int> sortArray(vector<int> array)
    {
        cout << "Initial Array: ";
        printArray(array);
    
        vector<vector<int>> even;
        vector<int> odd;
        vector<int> result;
        
        if(array.size() == 0){
          return array;
        } else {
          vector<int> place;
          
          for(unsigned int array_i = 0; array_i < array.size(); array_i++){
            place.clear();
            if(array[array_i]%2==0){ //EVEN
              place.push_back(array[array_i]);
              place.push_back(array_i);
            } else { //ODD
              odd.push_back(array[array_i]);
            }
            if(place.size() != 0){
              even.push_back(place);
            }
          }
          
          cout << "Odd values: ";
          printArray(odd);
          
          odd = sort(odd);
          cout << "Odd values: ";
          printArray(odd);
          
          cout << "Places... " << endl;
          for(unsigned int even_i = 0; even_i < even.size(); even_i++){
              cout << "Place array: ";
              printArray(even[even_i]);
          }
          
          for(unsigned int array_i = 0; array_i < array.size(); array_i++){
            if(array_i == even[0][1]){
              result.push_back(even[0][0]);
              even.erase(even.begin());
            } else {
              result.push_back(odd[0]);
              odd.erase(odd.begin());
            }
          }
        }
        
        return result;
    }
};

void printArray(const vector<int> &arr){
  cout << "[";
  
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    if(arr_i < arr.size()-1){
      cout << arr[arr_i] << ",";
    } else {
      cout << arr[arr_i] << "]" << endl;
    }
  }
}

vector<int> sort(vector<int> arr){
  int min = 0, temp = 0, minLocation = 0;

  for(unsigned int arr_i = 0; arr_i < arr.size()-1; arr_i++){
    min = arr[arr_i];
    minLocation = arr_i;
    for(unsigned int arr_j = arr_i; arr_j < arr.size(); arr_j++){
      if(arr[arr_j] < min){
        min = arr[arr_j];
        minLocation = arr_j;
      }
    }
    temp = arr[arr_i];
    arr[arr_i] = min;
    arr[minLocation] = temp;
  }
  
  return arr;
}
