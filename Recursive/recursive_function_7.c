#include <stdio.h>
unknown()
{
  int ch;
  if ((ch = getchar()) != '\n')
    unknown();
  putchar(ch);
}
int main(void)
{
  unknown();
  return 0;
}
