# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        """
                                    h1
            1 -> 4 -> 3 -> 2 -> 5 -> 2
            h2     f
            S: s-> 1 -> 2 -> 2
            F: s ->4 -> 3-> 5
                   s
        """
        dummyhead = ListNode(-1)  # -1  F

        dummyhead.next = head  # -1 -> 1 -> 4 -> 3 -> 2 -> 5 -> 2 -> #
        nodeLess, nodeGreater = dummyhead, dummyhead
        firstHead, secondHead = None, None
        while head:
            if head.val < x:
                nodeLess.next = ListNode(head.val)
                nodeLess = nodeLess.next
                if not firstHead:
                    firstHead = nodeLess
            else:
                nodeGreater.next = ListNode(head.val)
                nodeGreater = nodeGreater.next
                if not secondHead:
                    secondHead = nodeGreater
            head = head.next
    
        nodeLess.next = secondHead
        return firstHead

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(4)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(2)
    root.next.next.next.next = ListNode(5)
    root.next.next.next.next.next = ListNode(2)
    s = Solution()
    s.partition(root, 3)
