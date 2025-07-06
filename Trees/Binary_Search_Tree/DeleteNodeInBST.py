# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


def buildnode():
    # --- build the specific tree ---
    #
    #               6
    #             /   \
    #            4     7
    #          /   \    \
    #         1     3    10
    #                    /
    #                   8
    #

    # leaf nodes
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node8 = TreeNode(8)

    # interior nodes
    node4 = TreeNode(4, left=node1, right=node3)
    node10 = TreeNode(10, left=node8)
    node7 = TreeNode(7, right=node10)

    # root
    root = TreeNode(6, left=node4, right=node7)

    return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
              6
            /   \
            4    7
          /   \   \
         1     3   8

        [6, 4, 7, 8] # Nodes to be deleted

        BEFORE

              6
            /   \
            4    7
          /   \   \
         1     3    10
                   /
                   8
        [6, 4, 7, 8]

        1. check whether you're deleting a leaf node, single parent, node with 2 child
        Delete leaf node
        """
        if not root:
            return root

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        # Node to be deleted
        if root.val == key:
            # leaf node
            if not root.left and root.right:
                return None
            elif root.left and root.right:
                rightMostNode = self.findTheRightMostNode(root)
                root.right = self.deleteNode(root.right, rightMostNode.val)
                return rightMostNode
            else:
                if root.left:
                    rightMostNode = self.findTheRightMostNode(root)
                    root.right = self.deleteNode(root.right, rightMostNode.val)
                    return rightMostNode
                else:
                    leftMostNode = self.findTheLeftMostNode(root)
                    root.left = self.deleteNode(root.left, leftMostNode.val)
                    return leftMostNode
        return root

    def findTheRightMostNode(self, node):
        prev = None
        while node:
            prev = root
            if node.right:
                node = node.right
            else:
                node = node.left
        return prev

    def findTheLeftMostNode(self, node):
        prev = None
        while node:
            prev = root
            if node.left:
                node = node.left
            else:
                node = node.right
        return prev

if __name__ == '__main__':
    root = buildnode()

    # --- invoke your method ---
    sol = Solution()
    # e.g. delete key = 7
    new_root = sol.deleteNode(root, 7)
    # optional: simple preorder print to verify structure
    def preorder(n):
        if not n:
            return
        print(n.val, end=" ")
        preorder(n.left)
        preorder(n.right)

    preorder(new_root)