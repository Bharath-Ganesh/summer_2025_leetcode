# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    """
        P1  new_head
        P   C
            1 -> 2 -> 3 -> 4 -> 5 -> null
                 P1   C1   P    C
            2 -> 1 -> 4 -> 3.. -> 5 -> null

        1 <- 2 <- 3 <- 4 -> 5 -> null
        After reversal

        1 -> 4 -> 3 -> 2 -> 5 -> null

    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        k = 2
newHead initial_head
        1 -> 2 -> 3 -> 4 -> 5

             P   C
        1 <- 2 -> 3 -> 4 -> 5

        After loop
                        P   C
        2 -> 1 ->   4 -> 3-> 5
        newHead  initial_head
        """

        length = self.findLength(head)
        k = k % length
        newHead = None
        initial_head = head

        while k > 0:
            prev, curr = newHead, initial_head
            for i in range(k):
                if not curr:
                    continue
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            if newHead:
                newHead.next = prev  # TODO
            else:
                head = prev

            if initial_head:
                initial_head.next = curr
            newHead = initial_head
            initial_head = curr
            k -= 1
        return head

    def findLength(self, head):
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        return length

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    sol = Solution()
    sol.reverseKGroup(head, 2)
