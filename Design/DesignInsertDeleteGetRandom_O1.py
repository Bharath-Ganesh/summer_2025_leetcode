import random
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        # Whenever a missing key is accessed, __factory__() is called to produce its default value.
        self.look_up = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.look_up:
            return False
        index = len(self.arr)
        self.arr.append(val)
        self.look_up[val] = index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.look_up:
            return False
        n = len(self.arr)
        if n == 1:
            ele = self.arr[0]
            del self.look_up[ele]
            self.arr = []
            return True  # ==> MUST return here to avoid further logic

        last_element_index = n - 1
        last_element_val = self.arr[last_element_index]
        if val != last_element_val:
            curr_element_index = self.look_up[val]
            # update last element index
            self.look_up[last_element_val] = curr_element_index
            self.arr[curr_element_index] = last_element_val

        self.arr.pop()
        del self.look_up[val]
        return True

    def getRandom(self) -> int:
        lower = 0
        upper = len(self.arr) - 1
        random_index = random.randint(lower, upper)
        return self.arr[random_index]

if __name__ == '__main__':
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())