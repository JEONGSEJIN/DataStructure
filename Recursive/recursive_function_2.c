#include <stdio.h>
int sum(int n)
{
  printf("%d\n", n);
  if (n < 1) return 1;
  else return (n + sum(n - 1));
}
int main(void)
{
  int num;
  printf("%d\n", sum(5));
  return 0;
}
