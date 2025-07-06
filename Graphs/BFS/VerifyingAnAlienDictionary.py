from collections import defaultdict
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """

        "hello"
        "leetcode"
        "hlabcdefgijkmnopqrstuvwxyz"
        "h -> l -> e"

        words = ["word","world","row"],
        worldabcefghijkmnpqstuvxyz
        w -> o -> r -> l
        word    :
        world   :
        Invalid
        1. A -> B all characters are same , but length of A is larger.
        2. ord value of B is greater than A for the same index.

        Process:
        1. Take two words at a time
        2. Compare their rank, but before this create a rank using toposort, which gives linear ordering.
        """

        """
        hlabcdefgijkmnopqrstuvwxyz
        hello
        leetcode

        1. Create a lookup:
        2. if first == second and len(first) > second : false
        3. if first[]
        h = 0
        l = 1..
        """
        n = len(order)
        lookup = {order[idx] : idx for idx in range(n)}
        for first_word, second_word in zip(words[:n - 1], words[1:]):
            for i in range(len(second_word)):
                if i ==  len(first_word):
                    if first_word == second_word[:(i + 1)]:
                        return False
                    break

                if lookup[first_word[i]] > lookup[second_word[i]]:
                    return False
                elif lookup[first_word[i]] == lookup[second_word[i]]:
                    continue
                break
        return True

if __name__ == '__main__':
    solution = Solution()

    solution.isAlienSorted(   words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")