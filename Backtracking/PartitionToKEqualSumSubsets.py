from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
            sum = 20/K => 5 [4,3,2,3,5,2,1]
        """

        total_sum, max_sum = 0, 0
        for num in nums:
            total_sum += num
            max_sum = max(max_sum, num)

        partition_sum = total_sum // k
        if total_sum % k != 0 or max_sum > partition_sum:
            return False


        partition = [0] * k

        def backtrack(idx):
            if idx == len(nums):
                return True

            used_sums = set()  # track bucket sums we've tried at this level
            for j in range(k):
                # patch: skip if placing overflows or duplicates this sum
                # 1. This ensures that if two buckets currently have the same sum, you only try putting nums[idx] into one of them—because they’re interchangeable.
                # 2. Overflow check
                if partition[j] in used_sums or partition[j] + nums[idx] > partition_sum:
                    continue

                used_sums.add(partition[j])
                partition[j] += nums[idx]
                if backtrack(idx + 1):
                    return True
                partition[j] -= nums[idx]

                # patch: break if this bucket was empty—no need to try other empty buckets
                if partition[j] == 0:
                    break
            return False

        return backtrack(0)

if __name__ == '__main__':
    s = Solution()
    ans = s.canPartitionKSubsets(nums = [1, 1, 2, 1, 2, 2, 2, 1] , k = 4)      # True
    print(ans)
