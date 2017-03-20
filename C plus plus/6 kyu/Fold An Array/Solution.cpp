using namespace std;

class Kata
{
public:
    vector<int> foldArray(vector<int> array, int runs)
    {
        vector<int> result;
        
        for(int runs_i = 0; runs_i < runs; runs_i++){
          cout << "INPUT" << endl;
          printVector(array);

          if(array.size() % 2 == 0){
            int pivot = (array.size() / 2);
            for(int array_i = 0; array_i < pivot; array_i++){
              result.push_back(array[array_i] + array[array.size()-1-array_i]);
            }
          } else {
            int pivot = (array.size() / 2);
            for(int array_i = 0; array_i < pivot; array_i++){
              result.push_back(array[array_i] + array[array.size()-1-array_i]);
            }
            result.push_back(array[pivot]);
          }
          
          array.swap(result);
          result.clear();
          printVector(array);
        }    
        return array;
    }
    
    void printVector(vector<int> array){
      for(int array_i = 0; array_i < array.size(); array_i++){
        cout << array[array_i] << endl;
      }
    }
};
