class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        lps_arr = self.lps(needle)
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps_arr[j - 1]
                else:
                    i += 1

            if j == len(needle):
                return i - j

        return -1

    def lps(self, pattern):
        n = len(pattern)
        lps_arr = [0] * n
        lps = 0
        index = 1
        while index < n:
            if pattern[index] == pattern[lps]:
                lps_arr[index] = lps + 1
                lps += 1
                index += 1
            else:
                if lps != 0:
                    lps = lps_arr[lps - 1]
                else:
                    index += 1
        return lps_arr



if __name__ == '__main__':
    sol = Solution()
    ans = sol.strStr("mississippi","issip")
    print(ans)
