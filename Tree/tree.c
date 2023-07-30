#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode {
  int data;
  struct TreeNode * left, *right;
} TreeNode;

//             11
//       6            8
//   19     4      10   5
// 17  43 31  49  7  3 2  9
TreeNode n1 = { 17, NULL, NULL };
TreeNode n2 = { 43, NULL, NULL };
TreeNode n3 = { 19, &n1, &n2 };
TreeNode n4 = { 31, NULL, NULL };
TreeNode n5 = { 49, NULL, NULL };
TreeNode n6 = { 4, &n4, &n5 };
TreeNode n7 = { 7, NULL, NULL };
TreeNode n8 = { 3, NULL, NULL };
TreeNode n9 = { 10, &n7, &n8 };
TreeNode n10 = { 2, NULL, NULL };
TreeNode n11 = { 9, NULL, NULL };
TreeNode n12 = { 5, &n10, &n11 };
TreeNode n13 = { 6, &n3, &n6 };
TreeNode n14 = { 8, &n9, &n12 };
TreeNode n15 = { 11, &n13, &n14 };
TreeNode *root = &n15;

void smaller_Ndoe(TreeNode *root, int n)
{
  if (root != NULL)
  {
    smaller_Node(root->left, n);
    if (root->data < n)
    {
      printf("%d보다 작은 노드: %d\n", n, root->data);
    }
    smaller_Node(root->right, n);
  }
}

int main(void)
{
  int num;
  printf("값을 입력하시오: ");
  scanf("%d", &num);
  smaller_Ndoe(root, num);
  return 0;
}
