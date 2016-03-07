#include <stdio.h>


int main(int argc, char *argv[]){
  int bugs = 100;
  double bug_rate = 1.2;

  printf("You have %d bugs at the imaginary rate of %f.\n",
         bugs, bug_rate);

  long universe_of_defects = 1L * 1024L * 1024L * 1024L;
  printf("The entire universe has %ld bugs.\n",
         universe_of_defects);

  char nul_byte = '\0';
  int care_percentage = bugs * nul_byte;

  printf("Which means you should care %d%%.\n",
         care_percentage);
  printf("print char as string: %s", nul_byte);

  return 0;
}
