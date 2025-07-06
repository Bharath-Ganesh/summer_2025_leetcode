# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
              6
            /   \
            4    7
          /   \
         1     3

        [2, 5, 8, 0]
        """
        if not root:
            node = TreeNode(val)
            return node

        if root.val >= val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

if __name__ == '__main__':
    s = Solution()
    s.insertIntoBST(TreeNode(2), 2)