from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        h1, h2 = l1, l2
        head = ListNode(-1)
        h = head
        carry = 0
        while h1 or h2 or carry > 0:
            h1_val = 0 if not h1 else h1.val
            h2_val = 0 if not h2 else h2.val

            last_digit = (h1_val + h2_val + carry) % 10
            nextNode = ListNode(last_digit)
            head.next = nextNode
            head = head.next
            carry = (h1_val + h2_val + carry) / 10

            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next

        return h.next
