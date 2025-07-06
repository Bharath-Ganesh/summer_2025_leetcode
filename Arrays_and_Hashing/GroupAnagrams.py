from collections import defaultdict, Counter
from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def group_by_key(word):
            freq_arr = [0] * 26
            for ch in word:
                ascii_pos = ord(ch) - ord('a')
                freq_arr[ascii_pos] += 1

            key = ""
            for i in range(26):
                if freq_arr[i] > 0:
                    key += f"{chr(i + ord('a'))}{freq_arr[i]}"
            return key

        group_by_freq = defaultdict(list)
        for word in strs:
            group_by_freq[group_by_key(word)].append(word)
        return list(group_by_freq.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))