# Definition for a binary tree node.

from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        temp = []
        while queue:
            node = queue.popleft()
            if not node:
                temp.append("")
                continue
            if node:
                temp.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(temp)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        nodeData = data.split(",")
        n = len(nodeData)
        rootNode = TreeNode(int(nodeData[0]))
        idx = 1
        queue = deque()
        queue.append(rootNode)
        while idx < len(nodeData):
            root = queue.popleft()
            if idx < n and nodeData[idx] != "":
                leftNode = TreeNode(int(nodeData[idx]))
                root.left = leftNode
                queue.append(leftNode)
            idx += 1
            if idx < n and nodeData[idx] != "":
                rightNode = TreeNode(int(nodeData[idx]))
                root.right = rightNode
                queue.append(rightNode)
            idx += 1
        return rootNode

    def build_example_tree(self) -> TreeNode:
        #        1
        #       / \
        #      2   3
        #         / \
        #        4   5
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.right.left = TreeNode(4)
        root1.right.right = TreeNode(5)
        return root1
    # Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    ser = Codec()
    root = ser.build_example_tree()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))

