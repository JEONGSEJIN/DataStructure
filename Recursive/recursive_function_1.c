#include <stdio.h>
double recursive_function(double n)
{
  if (n == 1)
    return 1;
  else
    return 1 / n + recursive_function(n - 1);
}
int main(void)
{
  int num;

  printf("n의 값 입력: ");
  scanf("%d, &num);

  printf("1 + 1/2 + 1/3 + ... + 1/%d: %f\n", num, recursive_function(num));
  return 0;
}
