from collections import deque
from typing import List


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:

        word_set = set(deadends)
        if "0000" in word_set:
            return -1

        queue = deque()
        queue.append(([0, 0, 0, 0], 0))

        visited = set()
        visited.add((0, 0, 0, 0))

        while queue:
            element, operation = queue.popleft()
            num_str = "".join(map(str, element))
            if num_str == target:
                return operation

            for i in range(4):
                temp = element[:]
                temp[i] = (temp[i] + 1) % 10
                next_value = "".join(map(str, temp))
                next_list = tuple(temp)

                temp = element[:]
                if temp[i] == 0:
                    temp[i] = 9
                else:
                    temp[i] -= 1
                prev_value = "".join(map(str, temp))
                prev_list = tuple(temp)

                if next_value not in word_set and next_list not in visited:
                    visited.add(next_list)
                    queue.append((list(next_list), operation + 1))

                if prev_value not in word_set and prev_list not in visited:
                    visited.add(prev_list)
                    queue.append((list(prev_list), operation + 1))
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.openLock(["0201", "0101", "0102", "1212", "2002"],
                            "0202"))  # expected output e.g. 6 or -1 depending on deadends
