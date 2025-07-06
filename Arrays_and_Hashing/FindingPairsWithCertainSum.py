from collections import Counter
from typing import List


class FindSumPairs:
    """
        [1, 1, 2, 2, 2, 3], => (1 -> 2, (2 -> 3), (3))
        [1, 1, 2, 2, 2, 3] // should we hash it? Does BS help? freq map
        [1, 4, 5, 4, 5, 4] // can we hash it
        map (1:1, 2:0, 4:3, 5:2)
        [0, 1, 2, 3, 4, 5]
        1. Take two hash
        2.
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.nums1 = nums1
        self.lookup_num1 = Counter(nums1)
        self.lookup_num2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # When we add values, first reduce the current value and increment the new value
        if index >= len(self.nums2):
            return

        curr_value = self.nums2[index]
        self.lookup_num2[curr_value] -= 1
        if self.lookup_num2[curr_value] == 0:
            del self.lookup_num2[curr_value]
        updated_value = curr_value + val
        self.lookup_num2[updated_value] += 1


    def count(self, tot: int) -> int:
        total_pairs = 0
        for num, freq in self.lookup_num1.items():
            # second arr all value positive
            if num >= tot:
                continue
            net_value = tot - num
            if net_value in self.lookup_num2:
                total_pairs += (self.lookup_num2[net_value] * freq)

        return total_pairs

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

if __name__ == '__main__':
    findSumPairs = FindSumPairs([9,70,14,9,76],[26,26,58,23,74,68,68,78,58,26])
    findSumPairs.add(6,10)
    findSumPairs.add(5,6)
    print(findSumPairs.count(32))
    findSumPairs.add(3, 55)
    findSumPairs.add(9, 32)
    findSumPairs.add(9, 16)
    findSumPairs.add(1, 48)
    findSumPairs.add(1, 4)
    findSumPairs.add(0, 52)
    findSumPairs.add(8, 20)
    findSumPairs.add(9, 4)
    print(findSumPairs.count(88))
    print(findSumPairs.count(154))
