# include <stdio.h>
int asterisk(int i)
{
  if (i > 1) {
    asterisk(i / 2);
    asterisk(i / 2);
  }
  printf("*");
}
int main(void)
{
  int num;
  asterisk(5);
  return 0;
}
