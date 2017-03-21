void printVector(const std::vector<std::string> &);

class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        std::vector<std::string> result;
        
        for(unsigned int floor_i = 0; floor_i < nFloors; floor_i++){
          std::string line = "";
          
          for(unsigned int spaces = floor_i; spaces < nFloors-1; spaces++){
            line += " ";
          }
          
          for(unsigned int stars = 0; stars < 2*floor_i+1; stars++){
            line += "*";
          }
          
          for(unsigned int spaces = floor_i; spaces < nFloors-1; spaces++){
            line += " ";
          }
          
          result.push_back(line);
        }
        return result;
    }
};

void printVector(const std::vector<std::string> &arr){
  for(unsigned int arr_i = 0; arr_i < arr.size(); arr_i++){
    std::cout << "|" << arr[arr_i] << "|" << std::endl;
  }
}
