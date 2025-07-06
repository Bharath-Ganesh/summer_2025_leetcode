# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Pair:
    def __init__(self, val, node):
        self.val = val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        [[1,4,5],[1,3,4],[2,6]]
        1 -> 4 -> 5 -> null
        1 -> 3 -> 4 -> null
        2 -> 6 -> null
        """
        min_heap = []
        for idx, listNode in enumerate(lists):
            # unique sequence count
            if listNode:
                heap_pair = Pair(listNode.val, listNode)
                heapq.heappush(min_heap, heap_pair)

        dummyHead = ListNode(-1)
        dh = dummyHead
        while min_heap:

            p = heapq.heappop(min_heap)
            val, node = p.val, p.node
            newNode = ListNode(val)
            dh.next = newNode
            dh = dh.next
            if node and node.next:
                heapq.heappush(min_heap, Pair(node.next.val, node.next))

        return dummyHead.next

    def build_list(self, arr: List[int]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def print_list(self, node: Optional[ListNode]) -> None:
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print(" -> ".join(vals) if vals else "empty")


if __name__ == "__main__":
    # --- Construct the input lists ---
    s = Solution()
    lists_input = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists_nodes = [s.build_list(sub) for sub in lists_input]

    # --- Merge ---
    s = Solution()
    merged = s.mergeKLists(lists_nodes)

    # --- Display result ---
    s.print_list(merged)