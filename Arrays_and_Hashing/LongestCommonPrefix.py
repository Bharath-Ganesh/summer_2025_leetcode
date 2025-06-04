from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        """
            ["flow","flow","flig"]
        """
        if not words:
            return ""
        min_length = len(words[0])
        for word in words:
            min_length = min(len(word), min_length)

        lcp = 0
        for index in range(min_length):
            first_word = True
            char_to_be_matched = ''
            for word in words:
                if first_word:
                    char_to_be_matched = word[index]
                    first_word = False
                else:
                    if word[index] != char_to_be_matched:
                        return words[0][0:lcp]
            lcp += 1

        return words[0][0:lcp]



if __name__ == '__main__':
    sol = Solution()
    ans= sol.longestCommonPrefix(["flow", "flowasd", "flighest"])
    print(ans)