# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildNode(self):
        # Build the tree from the example:
        #
        #        3
        #       / \
        #      4   5
        #     / \   \
        #    1   3   1

        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        root.right.right = TreeNode(1)
        return root


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        max_robbed = [0, 0]
        queue.append(root)
        idx = 2
        while queue:
            size = len(queue)
            total_sum = 0
            for i in range(size):
                node = queue.pop()
                total_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_robbed.append(0)
            max_robbed[idx] = max(max_robbed[idx - 2] + total_sum, max_robbed[idx - 1])
            idx += 1
        return max_robbed[-1]

if __name__ == '__main__':
    sol = TreeNode()
    root = sol.buildNode()

    sol  = Solution()
    sol.rob(root)