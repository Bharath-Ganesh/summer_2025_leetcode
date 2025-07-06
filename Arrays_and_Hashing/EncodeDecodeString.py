from typing import List


class Solution:
    """
    Input: ["neet","code","love","you"]

    4#neet4#code4#love#3you
    4neetcode4love3you
    """

    def __init__(self):
        self.DELIMITER = '#'

    def encode(self, strs: List[str]) -> str:
        parts = [f"{len(word)}{self.DELIMITER}{word}" for word in strs]
        return "".join(parts)

    def decode(self, word) -> List[str]:
        if word == "":
            return []

        res = []
        length_of_word_in_str = ""
        index = 0
        while index < len(word):
            delimiter_pos = word.index('#', index)
            length = int(word[index:delimiter_pos])
            index = delimiter_pos + 1
            res.append(word[index:index + length])
            index += length 
        return res

if __name__ == '__main__':
    solution = Solution()
    strs = ["neet","code","love","you"]
    decode= solution.encode(strs)
    print(decode)
    print(solution.decode(decode))