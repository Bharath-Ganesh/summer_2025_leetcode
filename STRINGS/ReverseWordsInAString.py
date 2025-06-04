class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in the string `s`, where words are separated by spaces.
        Any leading, trailing, or multiple intermediate spaces should be reduced to a single space.

        Instead of manually parsing character by character, we can:
          1. Use str.split() to split on any whitespace (automatically removes extra spaces).
          2. Reverse the resulting list of words.
          3. Join them with a single space.

        This runs in O(n) time and uses minimal extra code.
        """
        # 1. s.split() → list of words (splits on all runs of whitespace, drops empties)
        words = s.split()

        # 2. Reverse the list of words
        reversed_words = words[::-1]

        # 3. Join with a single space
        return " ".join(reversed_words)


if __name__ == '__main__':
    s = Solution()
    ans = s.reverseWords("the                sky                    is blue")
    print(ans)