#include <string.h>

char *makeUpperCase (char *string);

char *makeUpperCase (char* string) {
  for (int string_index = 0; string_index < strlen(string); string_index++){
    string[string_index] = toupper(string[string_index]);
  }

  return string;
}
