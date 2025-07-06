# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        """
        prev L
        1 -> 2 -> 3 -> 4 -> 5 -> null
                       R
             h
                       p    c
        1 <- 2 <- 3 <- 4 -> 5 -> null
        After reversal

        1 -> 4 -> 3 -> 2 -> 5 -> null
        """
        prev_ptr = None
        new_head = head
        for i in range(left - 1):
            if not new_head:
                break
            prev_ptr = new_head
            new_head = new_head.next

        prev, curr = prev_ptr, new_head
        for i in range(left, right + 1):
            if not curr:
                break
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        if prev_ptr:
            prev_ptr.next = prev
        else:
            head = prev
        if new_head:
            new_head.next = curr
        return head

    def print_list(self, node: ListNode) -> None:
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print(" -> ".join(vals))
    def constructListnode(self, values):
        # Given array and bounds
        # Build the linked list
        dummy = ListNode(0)
        tail = dummy
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next

        return dummy.next
if __name__ == '__main__':
    s = Solution()
    values = [1, 2, 3, 4, 5]
    left, right = 2, 4
    head = s.constructListnode(values)
    ans = s.reverseBetween(head, left, right)
    s.print_list(ans)
