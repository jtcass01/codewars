using namespace std;

string pattern(int n) {  
    string result = "";
    
    if(n == 1){
      return "1";
    }
    
    for(int n_i = 0; n_i < n; n_i++){
      cout << n_i << endl;
      for(unsigned int n_j = n_i; n_j < n-1; n_j++){
//        cout << "Space count = " << n_i << endl; 
        result += " ";
      }
      
      for(unsigned int n_j = 1; n_j < (n_i)+2; n_j++){
        result += to_string(n_j%10);
      }

      for(unsigned int n_j = n_i; n_j > 0; n_j--){
        result += to_string(n_j%10);
      }

      for(unsigned int n_j = n_i; n_j < n-1; n_j++){
        result += " ";
//        cout << "Space count = " << n_i << endl; 
      }

      if(n_i != n-1){
        result += "\n";
      }
    }
    
    cout << result << endl;
    return result;
}
