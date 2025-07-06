from typing import List



class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
            ["a","b","ba","bca","bda","bdca"]
              1,  1,  2,  3,  3 , 4
        """
        words.sort(key=lambda x: len(x))
        n = len(words)
        max_length = 1
        length_arr = [1] * n
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if len(words[j]) + 1 == len(words[i]):
                    if self.check_predecessor(i, j, words):
                        if length_arr[i] < length_arr[j] + 1:
                            length_arr[i] = length_arr[j] + 1
                            max_length = max(max_length, length_arr[i])

        return max_length

    def check_predecessor(self, i, j, words):
        curr_word = words[i]
        predecessor = words[j]
        ind1, ind2 = 0, 0
        while ind1 < len(curr_word) and ind2 < len(predecessor):

            if curr_word[ind1] == predecessor[ind2]:
                ind1 += 1
                ind2 += 1
            else:
                ind1 += 1
        return ind2 == len(predecessor)



if __name__ == '__main__':
    s = Solution()
    print(s.longestStrChain(["sgtnz","sgtz","sgz","ikrcyoglz","ajelpkpx","ajelpkpxm","srqgtnz","srqgotnz","srgtnz","ijkrcyoglz"]))