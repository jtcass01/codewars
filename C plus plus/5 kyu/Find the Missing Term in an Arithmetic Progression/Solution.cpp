using namespace std;

static long findMissing(std::vector<long> list){
  vector<long> differences;
  long minChange = list[0];
  
  if(list.size() > 1){
    minChange = abs(list[0] - list[1]);
  }
  
  for(unsigned int list_i = 0; list_i < list.size()-1; list_i++){
    differences.push_back(list[list_i+1]-list[list_i]);
  }
  
  for(unsigned int differences_i = 0; differences_i < differences.size(); differences_i++){
    if(abs(differences[differences_i]) <= minChange){
      minChange = abs(differences[differences_i]);
      break;
    }
  }
  
  if(list[0] > list[1]){
    for(unsigned int list_i = 0; list_i < list.size()-1; list_i++){
      if(list[list_i]-list[list_i+1] != minChange){
        return list[list_i] - minChange;
      }
    }
  } else {
    for(unsigned int list_i = 0; list_i < list.size()-1; list_i++){
      if(list[list_i+1]-list[list_i] != minChange){
        return list[list_i] + minChange;
      }
    }
  }
}

long abs(long value){
  if(value < 0){
    return value *= -1;
  } else {
    return value;
  }
}
