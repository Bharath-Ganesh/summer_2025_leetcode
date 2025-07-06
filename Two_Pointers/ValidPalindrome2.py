class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
         abcccecba
        """

        def back_track(left, right, count):
            if count > 1:
                return False

            if left >= right:
                return True

            if s[left] != s[right]:
               return  back_track(left, right - 1, count + 1) or back_track(left + 1, right, count + 1)
            else:
                return back_track(left + 1, right - 1, count)

        return back_track(0, len(s) - 1, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("bddb") == True)