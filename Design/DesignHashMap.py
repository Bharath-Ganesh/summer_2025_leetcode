class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.MOD = 10 ** 4
        self.hash_map = [None] * self.MOD

    def put(self, key: int, value: int) -> None:
        idx = key % self.MOD
        if not self.hash_map[idx]:
            self.hash_map[idx] = ListNode(key, value)
            return

        curr = self.hash_map[idx]
        while curr:
            if curr.key == key:
                # overwrite existing
                curr.val = value
                return
            if not curr.next:
                break
            curr = curr.next

        # append new node
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.MOD
        curr = self.hash_map[idx]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.MOD
        curr = self.hash_map[idx]
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    # FIX: update head to curr.next, not None
                    self.hash_map[idx] = curr.next
                return
            prev, curr = curr, curr.next
