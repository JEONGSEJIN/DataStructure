#include <stdio.h>
int recursive(int n)
{
  if (n != 1) recursive(n - 1);
  printf("%d\n", n);
}
int main(void)
{
  int num;
  recursive(5);
  return 0;
}
