using namespace std;

std::string is_sorted_and_how(std::vector<int> array) {
  int result = 3, last = 0;
  
  for(unsigned int array_i = 0; array_i < array.size(); array_i++){
    if(array_i == 0){
      last = array[array_i];
    } else {
      if(last < array[array_i]){
        if(result == 3 || result == 1){
          result = 1;
        } else {
          result = 0;
        }
      } else if (last > array[array_i]) {
        if (result == 3 || result == 2){
          result = 2;
        } else {
          result = 0;
        }
      }
    }
  }
  
  switch(result){
    case 0:
      return "no";
    case 1:
      return "yes, ascending";
    case 2:
      return "yes, descending";
  }
}
