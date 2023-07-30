#include <stdio.h>
int recursive(int n)
{
  printf("%d\n", n);
  if (n < 1) return -1;
  else return (recursive(n - 3) + 1);
}
int main(void)
{
  int num;
  printf("%d\n", recursive(10));
  return 0;
}
