#include <stdio.h>

int main(int argc, char *argv[])
{
  int areas[] = {10, 12, 13, 14, 20};
  char name[] = "Zed";
  char full_name[] = "Zed A. Shaw";
  printf("The size of an int: %ld\n", sizeof(int));
  printf("The size of areas (int[1]): %ld\n", sizeof(areas));
  printf("The number of ints in areas: %ld\n",
         sizeof(areas) / sizeof(int));
  printf("sizeof char %d.\n", sizeof(char));
  printf("nums of char %d", sizeof(full_name) / sizeof(char) - 1);
  return 0;
}
