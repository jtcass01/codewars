#define true 1
#define false 0
#define bool int

char* longest(char* s1, char* s2) {
  int s1_l = 0, s2_l = 0, max_l = 0, found_count = 0;

  s1_l = StringLength(s1);
  s2_l = StringLength(s2);
  
  max_l = s1_l + s2_l;
  
  char result[max_l];

  for(char ascii_value = 97; ascii_value < (char)123; ascii_value++){
    int s1_index = 0, s2_index = 0;
    bool notFound = true;
    
    while ((*(s1 + s1_index) != '\0' || *(s2 + s2_index) != '\0') && notFound) {
      if(*(s1 + s1_index) != '\0'){
        if( *(s1 + s1_index) ==  ascii_value) {
          *(result + found_count) = ascii_value;
          found_count++;
          notFound = false;
        }
        s1_index++;
      }
      
      if(*(s2 + s2_index) != '\0'){
        if( *(s2 + s2_index) ==  ascii_value) {
          *(result + found_count) = ascii_value;
          if(notFound) {
            found_count++;
          }
          notFound = false;
        }
        s2_index++;
      }  
    }
  }
  
  *(result + found_count) = '\0';

  return result;
}

int StringLength(const char *string){
  int size;
  
  for(size = 0; *(string + size) != '\0'; size++){
  }
  
  return size;
}
