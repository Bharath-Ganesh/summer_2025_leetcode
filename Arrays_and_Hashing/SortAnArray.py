from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we can use sorting algorithm
        # quick sort or merge sort
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sorted_array(self, nums, left, mid, right):
        ind1 = left
        ind2 = mid
        ind = left
        arr = [0] * len(nums)
        while ind1 <= mid - 1 and ind2 <= right:
            if nums[ind1] <= nums[ind2]:
                arr[ind] = nums[ind1]
                ind1 += 1
            else:
                arr[ind] = nums[ind2]
                ind2 += 1
            ind += 1

        while ind1 <= mid - 1:
            arr[ind] = nums[ind1]
            ind += 1
            ind1 += 1

        while ind2 <= right:
            arr[ind] = nums[ind2]
            ind += 1
            ind2 += 1

        for i in range(left, right + 1):
            nums[i] = arr[i]
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return nums
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        return self.merge_sorted_array(nums, left, mid + 1, right)

if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([0]))