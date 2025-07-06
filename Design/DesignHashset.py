class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None

class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.mod = 10 ** 4
        self.hash_set = [ None for i in range(self.mod)]

    def add(self, key: int) -> None:
        curr_head = self.hash_set[key % self.mod]
        if not curr_head:
            curr_head = ListNode(key)
            self.hash_set[key % self.mod] = curr_head
            return

        prev = None
        while curr_head:
            if curr_head.key == key:
                return
            prev = curr_head
            curr_head = curr_head.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr_head = self.hash_set[key % self.mod]
        if not curr_head:
            return
        prev = None
        while curr_head:
            if curr_head.key == key:
                if not prev:
                    self.hash_set[key % self.mod] = self.hash_set[key % self.mod].next
                else:
                    prev.next = curr_head.next
                return
            prev = curr_head
            curr_head = curr_head.next

    def contains(self, key: int) -> bool:
        curr_head = self.hash_set[key % self.mod]
        if not curr_head:
            return False

        while curr_head:
            if curr_head.key == key:
                return True
            curr_head = curr_head.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)